# Problème azure AD : comportement étrange entre création et update d'un user

**URL:** https://community.simplicite.io/t/4029

## Question
Bonjour,
j'utilise le code suivant pour créer ou mettre un jour un utilisateur depuis un ad Azure.
Le problème c'est que ce soit avec 
if (!Grant.exists(login, false) ou String userId = getUserIdIfExist(login); 
le traitement considère dans le preLoadGrant l'utilisateur est toujours considéré comme existant ce qui n'est pas le cas.
Il passe donc dans le traitement de mise à jour updateUser mais là 
if (!usr.select(uid)) retourne false et donc le traitement s'arrete si je met 

'        String uid = getUserIdIfExist(login);
        if (StringUtils.isEmpty(uid)){
            return null;
        }
'
alors au moment de bUserTools.getForUpdate(uid); il est en erreur.

Est ce que vous auriez une explication sur le fait que le traitement ne passe pas dans le createUser ?
Une fois le traitement terminée le user est crée mais il n'a pas de responsabilité ce qui est logique le traitement sort avant.
J'ai executé plusieurs fois le code en debug avec différents comptes avec toujours le même résultat.

Version :
[Platform]
Status=OK
Version=5.1.7
BuiltOn=2021-10-11 21:23
Git=release/06df144aad08d1dc84d135cbaa736e153d26a617
Encoding=UTF-8
EndpointIP=172.20.0.3
EndpointURL=http://4b2345910247:8080
```
package com.simplicite.commons.ladnext;

import com.simplicite.util.*;
import com.simplicite.util.exceptions.AuthenticationException;
import com.simplicite.util.exceptions.GetException;
import com.simplicite.util.tools.BusinessObjectTool;
import org.apache.commons.lang3.StringUtils;
import org.apache.http.HttpEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import org.json.JSONArray;
import org.json.JSONObject;

import java.nio.charset.StandardCharsets;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Grant Hooks for Azure AD / Open ID Connect The call flow is 1. parseAuth => using the ID token,
 * we change the opaque login by the upn (User Principal Ladom), that is also the email 2.
 * preLoadGrant => we get the access token, then we call the Graph API and create or update the user
 * and its attributes 3. postLoadGrant => we do nothing for the moment
 *
 * <p>SessionInfo contains - getToken => access token - getIDToken => ID token - getRefreshToken =>
 * refresh token
 */
public class PlatformHooks extends PlatformHooksInterface {

    private static final String LADNEXT_MODULE = "ladnext_users";
    private static final String LADNEXT_HOME = "LadnextHome";
    private static final String ATT_USER_PRINCIPAL_LADNEXT = "userPrincipalName";
    private static final String ATT_USER_JOB_TITLE = "jobTitle";
    public static final String ATT_ROLE_MAPPER_TITRE = "titre";
    public static final String ATT_ROLE_MAPPER_DEPARTMENT = "department";
    public static final String ATT_ROLE_MAPPER_GROUPE = "groupe";

    /**
     * Call the Microsoft Graph API using the OIDC access token. Note that the lifetime of an access
     * token is short. If needed, get a new access token using the OIDC refresh token. This is
     * explained at
     * https://docs.microsoft.com/fr-fr/azure/active-directory/develop/v2-oauth2-auth-code-flow
     *
     * <p>See https://developer.microsoft.com/en-us/graph/graph-explorer for the format of the
     * queries e.g. sQuery = "https://graph.microsoft.com/v1.0/me" sQuery =
     * "https://graph.microsoft.com/v1.0/me/?$select=givenName,surname,jobTitle,department,officeLocation,city,postalCode";
     *
     * @param accessToken OIDC access token
     * @param sQuery Query for the Graph API
     * @return Returns a JSON object with the required attributes, returns null if an error occured
     */
    private JSONObject getMicrosoftGraphAPIAttributes(String accessToken, String sQuery) {
        // JSON returned by the Microsoft Graph API
        JSONObject graphObject = null;

        // call the Microsoft Graph API
        CloseableHttpClient httpClient = HttpClients.createDefault();

        try {
            HttpGet request = new HttpGet(sQuery);
            // add authorization request header (use the OIDC access token)
            request.setHeader("Authorization", "Bearer " + accessToken);
            request.setHeader("Content-Type", "application/json");

            // get response
            CloseableHttpResponse response = httpClient.execute(request);

            // The underlying HTTP connection is still held by the response object
            // to allow the response content to be streamed directly from the network socket.
            // In order to ensure correct deallocation of system resources
            // the user MUST call CloseableHttpResponse#close() from a finally clause.
            // Please note that if response content is not fully consumed the underlying
            // connection cannot be safely re-used and will be shut down and discarded
            // by the connection manager.

            if (200 == response.getStatusLine().getStatusCode()) {
                // HttpResponse Status is HTTP/1.1 200 OK
                try {
                    // get the response, assume its JSON and UTF8 encoded
                    HttpEntity entity = response.getEntity();
                    // use org.apache.http.util.EntityUtils to read json as string
                    String json = EntityUtils.toString(entity, StandardCharsets.UTF_8);
                    graphObject = new JSONObject(json);
                    // ensure the stream fully consumed
                    EntityUtils.consume(entity);
                } finally {
                    response.close();
                }
            } else {
                throw new AuthenticationException(
                        "Unable to call Microsoft Graph API, status code is "
                                + response.getStatusLine().toString());
            }

            httpClient.close();

        } catch (Exception e) {
            AppLog.error("getGraphAPIAttributes - exception ", e, null);
        }

        return graphObject;
    }

    /**
     * Get the Azure AD attributes if available or set to "" if not available
     *
     * @param graphObject Microsoft Graph API JSON response
     * @param adField Graph API / Azure AD field
     */
    private String getADFieldValue(JSONObject graphObject, String adField) {
        if (graphObject.has(adField) && !graphObject.isNull(adField)) {
            // is it an array ?
            JSONArray jsonArray = graphObject.optJSONArray(adField);
            if (jsonArray != null) {
                // keep the first element
                if (!jsonArray.isNull(0)) {
                    return jsonArray.getString(0);
                } else {
                    return "";
                }
            } else {
                // most probable case
                return graphObject.getString(adField);
            }
        }
        return "";
    }

    /**
     * Given Ladnext role, assign the user to groups
     *
     * @param usr User DB object
     * @param role Ladnext role
     * @return Returns true if successful, returns false otherwise
     */
    private boolean setUserResponsibilities(ObjectDB usr, PlatformHooks.LadomRole role, Grant g)
            throws Exception {
        AppLog.info("Begin - setUserResponsibilities " + usr.getRowId() + " role " + role, null);

        Grant.removeAllResponsibilities(usr.getRowId());

        // use this Ladnext role to assign the group
        if (role != null && !Tool.isEmpty(role.getGroup())) {

            boolean respAssociated =
                    Grant.addResponsibility(
                            usr.getRowId(),
                            role.getGroup(),
                            Tool.getCurrentDate(-1),
                            "",
                            true,
                            LADNEXT_MODULE);
            if (!respAssociated) {
                throw new Exception("Responsibility not added");
            } else {
                AppLog.info("preLoadGrant : Added " + role.getGroup() + 
                " responsibility for user " + usr.getRowId(),
                        null);
            }
        }

        return true;
    }

    /**
     * Create a new Ladnext user, then assign Ladnext groups to the user according to the following
     * attributes : - the jobTitle - the department - the company or the city
     *
     * @param login This is the userPrincipalName a.k.a. "upn" in OIDC
     * @param graphObject Microsoft Graph API JSON response
     * @param role : Ladnext Role
     * @return Returns userId if success, null if failed
     */
    private String createUser(String login, JSONObject graphObject, PlatformHooks.LadomRole role, Grant g) {
        /*
        Singleton to use system objects with Local access
        Be careful to use it in thread safe methods	or only to read parameters, or to execute direct SQL queries/updates
        */

        AppLog.info("Begin createUser login " + login, null);
                
        Grant sys = Grant.getSystemAdmin();

        try {
            ObjectDB usr = sys.getTmpObject("LadomUser");
            synchronized (usr) { // thread-safe
                // initialize the user
                // ----------------------------------------------------------
                usr.resetValues(true);
                usr.setRowId(ObjectField.DEFAULT_ROW_ID);
                usr.setStatus(Grant.USER_ACTIVE); // set user as 'active'

                // Module of the user
                String ladnextModuleId = ModuleDB.getModuleId(LADNEXT_MODULE);
                usr.setFieldValue("row_module_id", ladnextModuleId);
                usr.setFieldValue("row_module_id.mdl_name", LADNEXT_MODULE);
                usr.setFieldValue("usr_home_id",View.getViewId(sys.getParameter("DEFAULT_USER_HOME", LADNEXT_HOME)));

                // Properties
                usr.setFieldValue("usr_login", login);
                usr.setFieldValue("usr_lang", Globals.LANG_FRENCH); // MUST BE to a SimplicitÃ© format
                //usr.setFieldValue("usr_country", "FR"); // MUST BE to a SimplicitÃ© format
                //usr.setFieldValue("usr_lang_pref", Globals.LANG_FRENCH);
                usr.setFieldValue("usr_image_id", "");

                // Contact
                usr.setFieldValue("usr_first_name", getADFieldValue(graphObject, "givenName"));
                usr.setFieldValue("usr_last_name", getADFieldValue(graphObject, "surname"));
                usr.setFieldValue("usr_email",getADFieldValue(graphObject, ATT_USER_PRINCIPAL_LADNEXT)); // "mail" is null but this is the upn
                                                              // ...
                usr.setFieldValue("usr_cell_num", getADFieldValue(graphObject, "mobilePhone"));
              //  usr.setFieldValue("usr_work_num", getADFieldValue(graphObject, "businessPhones"));

                // Address
                //usr.setFieldValue("usr_address1", getADFieldValue(graphObject, "streetAddress"));
                //usr.setFieldValue("usr_address2", getADFieldValue(graphObject, "officeLocation"));
                //usr.setFieldValue("usr_city", getADFieldValue(graphObject, "city"));
                //usr.setFieldValue("usr_zipcode", getADFieldValue(graphObject, "postalCode"));

                // Tite de l'agent
                usr.setFieldValue("ladUsrTitre", getADFieldValue(graphObject, ATT_USER_JOB_TITLE));
                usr.setFieldValue("ladUsrDepartement", getADFieldValue(graphObject, ATT_ROLE_MAPPER_DEPARTMENT));

                // create the user in DB and get a row id
                // ----------------------------------------------------------
                new BusinessObjectTool(usr).validateAndCreate();

                // DEBUG
                AppLog.info("createUser : Created user " + usr.getRowId(), null);

                // assign groups
                // ----------------------------------------------------------
                setUserResponsibilities(usr, role, g);
                
                AppLog.info("End createUser login " + login, null);
                        
            } // synchronized

            return usr.getRowId();

        } catch (Exception e) {
            AppLog.error("preLoadGrant: unable to create user ", e, null);
            return null;
        }
    }

    /**
     * Update a Ladnext user Each time a user log in, we need to update its rights according to the
     * Azure AD information
     *
     * @param login This is the OIDC userPrincipalName
     * @param graphObject Microsoft Graph API JSON response
     * @param role : Ladnext Role
     * @return Returns user id if successful, returns null otherwise
     */
    private String updateUser(String login, JSONObject graphObject, PlatformHooks.LadomRole role, Grant g) {
        /*
        Singleton to use system objects with Local access
        Be careful to use it in thread safe methods	or only to read parameters, or to execute direct SQL queries/updates
        */
        
        AppLog.info("Begin updateUser login " + login, null);
          
        Grant sys = Grant.getSystemAdmin();
        // get the user id
        //String uid = sys.simpleQuery("select row_id from m_user where usr_login = '" + login + "'");
        //AppLog.info("AzureAD - updateUser using - uid = " + uid, null);
        String uid = getUserIdIfExist(login);
        if (StringUtils.isEmpty(uid)){
            return null;
        }

        try {
            ObjectDB usr = sys.getTmpObject("LadomUser");
            //if (!usr.select(uid)) {
            //    return null;
            //}
            BusinessObjectTool bUserTools = new BusinessObjectTool(usr);
            try{
                bUserTools.getForUpdate(uid);
            }
            catch (GetException e){
                AppLog.error(getClass(), "GetException", e.getMessage(), null,
                        null);
            }

            synchronized (usr) { // thread-safe
                usr.setStatus(Grant.USER_ACTIVE); // set user as 'active'

                // Properties
                usr.setFieldValue("usr_lang", Globals.LANG_FRENCH); // MUST BE to a SimplicitÃ© format
                //usr.setFieldValue("usr_country", "FR"); // MUST BE to a SimplicitÃ© format
                //usr.setFieldValue("usr_lang_pref", Globals.LANG_FRENCH);
                usr.setFieldValue("usr_image_id", "");

                // Module of the user
                String ladnextModuleId = ModuleDB.getModuleId(LADNEXT_MODULE);
                usr.setFieldValue("row_module_id", ladnextModuleId);
                usr.setFieldValue("row_module_id.mdl_name", LADNEXT_MODULE);
                usr.setFieldValue("usr_home_id",
                        View.getViewId(sys.getParameter("DEFAULT_USER_HOME", LADNEXT_HOME)));

                // Contact
                usr.setFieldValue("usr_first_name", getADFieldValue(graphObject, "givenName"));
                usr.setFieldValue("usr_last_name", getADFieldValue(graphObject, "surname"));
                usr.setFieldValue("usr_email",
                        getADFieldValue(graphObject, ATT_USER_PRINCIPAL_LADNEXT)); // "mail" is null but this is the upn
                                                              // ...
                usr.setFieldValue("usr_cell_num", getADFieldValue(graphObject, "mobilePhone"));
                //usr.setFieldValue("usr_work_num", getADFieldValue(graphObject, "businessPhones"));

                // Address
                //usr.setFieldValue("usr_address1", getADFieldValue(graphObject, "streetAddress"));
                //usr.setFieldValue("usr_address2", getADFieldValue(graphObject, "officeLocation"));
                //usr.setFieldValue("usr_city", getADFieldValue(graphObject, "city"));
               // usr.setFieldValue("usr_zipcode", getADFieldValue(graphObject, "postalCode"));

                // Tite de l'agent
                usr.setFieldValue("ladUsrTitre", getADFieldValue(graphObject, ATT_USER_JOB_TITLE));
                usr.setFieldValue("ladUsrDepartement", getADFieldValue(graphObject, ATT_ROLE_MAPPER_DEPARTMENT));

                // update the user in DB
                // ----------------------------------------------------------
                bUserTools.validateAndUpdate();

                // assign groups
                // ----------------------------------------------------------
                setUserResponsibilities(usr, role, g);
                
                AppLog.info("End updateUser login " + login, null);
                 
            } // synchronized

            return usr.getRowId();

        } catch (Exception e) {
            AppLog.error("preLoadGrant: unable to update user " + uid, e, null);
            return null;
        }
    }

    private String getUserIdIfExist(String login) {
        String uid = "";
        try {
            Grant sys = Grant.getSystemAdmin();
            uid = sys.simpleQuery("select row_id from m_user where usr_login = '" + login + "'");
            AppLog.info("isUserExist using - uid = " + uid, null);
        }catch (Exception e) {
            AppLog.error(getClass(), "isUserExist",
                    "Erreur lors du test de l'existence de l'utilisateur " + login,
                    null, null);
            return uid;
        }
        return uid;
    }

    /**
     * This method is called for parsing authentication string to extract user login. The login is
     * updated using the upn field of the ID token.
     *
     * @param sys System admin grant
     * @param info Session info
     * @return Returns the new login if successful, returns info.getLogin() otherwise
     */
    @Override
    public String parseAuth(Grant sys, SessionInfo info) {
        AppLog.info("Begin - parseAuth " + sys.getAuthProvider(), null);
		AppLog.info("parseAuth SessionInfo:" + info , null);
		
        if ((null == info) || (null == info.getIDToken())) {
            // do nothing, if we use a local login, the ID token should be null
            // we could also use info.getProvider() to get the OIDC provider name
            return null == info ? "" : info.getLogin();
        }
        String login = info.getLogin(); // get login as set by the IdP (sub field by default)

        try {
            // get the ID token as JWT
            String idToken = info.getIDToken();
            // NB: you can decode idToken using htltps://jwt.ms/

            // if we use a local login, the ID token is null and we won't change the login
            if (!Tool.isEmpty(idToken)) {
                // get the decoded ID token as a JSON object
                AppLog.info("parseAuth - Decode ID token and get payLoad", null);
                java.util.Base64.Decoder decoder = java.util.Base64.getUrlDecoder();
                String[] parts =
                        idToken.split("\\."); // split out the "parts" (header, payload and signature)

                String payload = new String(decoder.decode(parts[1]));
                JSONObject payLoadJson = new JSONObject(payload);
                String upn = payLoadJson.optString("upn");

				AppLog.info("parseAuth - upn " + upn, null);
 
                if (upn != null && !upn.isEmpty()) {
                    login = upn;
                } else {
                    throw new Exception("Could not parse login from token");
                }
            }
        } catch (Exception e) {
            AppLog.error("parseAuth - exception", e, null);
            login = ""; // must return empty string, not null, to tell the auth is rejected
        }
        AppLog.info("End - parseAuth : Setting login OK ", null);

        return login;
    }

    /**
     * This method is called before loading grant
     *
     * @param g Grant (mostly empty when calling this function)
     */
    public void preLoadGrant(Grant g) {
        AppLog.info("Begin preLoadGrant g " + g.toString(), null);

		// Pas de règles specifiques
		if (Grant.isTechnicalUser(g.getLogin()))
			return;
		
        // the method 'preLoadGrant' can be called even if the user is not logged ? try to check
        // this case
        // check also the authentication method : we must have a valid ID token when using OIDC
        // the method 'preLoadGrant' can be called even if the user is not logged ? try to check
        // this case
        // check also the authentication method : we must have a valid ID token when using OIDC
        SessionInfo info = g.getSessionInfo();
        if ((null == info) || (null == info.getIDToken())) {
            AppLog.info("Failed to retrieve informations", null);
            return;
        }
        // Microsoft Graph API: user attributes we need on return
        // note that the possibilities are limited :
        // https://docs.microsoft.com/en-us/graph/query-parameters
        // to test a query, see also https://developer.microsoft.com/en-us/graph/graph-explorer
        String sQueryAttributes =
                "https://graph.microsoft.com/v1.0/me/?$select=userPrincipalName,givenName,surname,mail,mobilePhone,businessPhones,jobTitle,department,companyName,officeLocation,streetAddress,city,postalCode,country";

        // call the Microsoft Graph API using the access token
        JSONObject graphObject = getMicrosoftGraphAPIAttributes(info.getToken(), sQueryAttributes);

        AppLog.info("Graph object:" + graphObject, null);
        // only if OIDC authentication method is used and the access token was valid
        if (null != graphObject) {
            try {
                // Set the login as the email (instead of the default opaque ID given by Azure AD)
                String login = graphObject.getString(ATT_USER_PRINCIPAL_LADNEXT);
                if (Tool.isEmpty(login)) {
                    throw new AuthenticationException("Empty login");
                }
                // retrieve Ladnext role given AD information
                PlatformHooks.LadomRole role = getUserRoleByADinfo(graphObject);

                String userId = getUserIdIfExist(login);
                AppLog.info("preLoadGrant : userId user " + userId + " login " + login, null);

	            if (StringUtils.isEmpty(userId)){
                //if (!Grant.exists(login, false)) {
	                 // create the user in database
	                 AppLog.info("AzureAD - preLoadGrant : Creating user ", null);
	                 userId = createUser(login, graphObject, role, g);
	            } else {
	                 // update user attributes in database
	                 AppLog.info("AzureAD - preLoadGrant : Updating user ", null);
	                 userId = updateUser(login, graphObject, role, g);
	            }

                g.setLang(Globals.LANG_FRENCH);
                g.setLangPreference(Globals.LANG_FRENCH);

            } catch (Exception e) {
                AppLog.error("preLoadGrant - exception", e, null);
                throw new RuntimeException("Could'not login properly.", e);
            }
            AppLog.info("End preLoadGrant: " + g, null);
        }
    }

    /**
     * Given AD information, retrieve the Ladnext role that matches the AD Information of the user
     * or null if no match has been found
     *
     * @param graphObject Microsoft Graph API JSON response
     * @return returns a Ladnext role or null
     */
    public PlatformHooks.LadomRole getUserRoleByADinfo(JSONObject graphObject) {
        // get the jobTitle and the city
        String jobTitle = getADFieldValue(graphObject, ATT_USER_JOB_TITLE);
        String department = getADFieldValue(graphObject, ATT_ROLE_MAPPER_DEPARTMENT);
		
		AppLog.info("Begin getUserRoleByADinfo - jobTitle : " + jobTitle + " department " + department , null);
		     
        LadomRoleMapper.RoleInfo roleInfo =
                new LadomRoleMapper().getRoleInfo(LadomRoleMapper.JOB_TITLE, jobTitle);
        PlatformHooks.LadomRole ladomRole = new PlatformHooks.LadomRole();
        ladomRole.setGroup(roleInfo.getGroup());
        
        AppLog.info("End getUserRoleByADinfo: " + ladomRole.getGroup() , null);
        
        return ladomRole;
    }

    /** This method is called after loading grant */
    public void postLoadGrant(Grant g) {
        AppLog.info("AzureAD - postLoadGrant " + g.toString() , null );

		// Pas de règles specifiques
		if (Grant.isTechnicalUser(g.getLogin()))
			return;


        // the method 'postLoadGrant' can be called even if the user is not logged, try to check
        // this case
        // check also if the authentication method OAuth2
        SessionInfo info = g.getSessionInfo();

        AppLog.debug("AzureAD - postLoadGrant info " + info);
        if ((null == info) || !g.isOAuth2AuthMethod()) {
            AppLog.debug("AzureAD - postLoadGrant : not logged");
        }

    }

    /**
     * Given the list job title, retrieve the user group that matches them or null if no match has
     * been found
     *
     * @param jobTitles list of job titles
     * @return returns a user group
     */
    private Set<String> getUserGroupsByAgentTitles(List<String> jobTitles) {
        AppLog.info("PlatformHooks - getUserGroupsByAgentTitles : " + jobTitles, null);
        
        Set<String> userGroups = new HashSet<>();

        // get the role map based on jobTitle
        JSONArray roleMapper = Grant.getSystemAdmin().getJSONArrayParameter("LADOM_ROLE_MAPPER");
        if (roleMapper != null) {
            for (int i = 0; i < roleMapper.length(); ++i) {
                JSONObject role = roleMapper.getJSONObject(i);
                if (role.has(ATT_ROLE_MAPPER_TITRE)
                        && jobTitles.contains(role.getString(ATT_ROLE_MAPPER_TITRE))
                        && role.has(ATT_ROLE_MAPPER_GROUPE)) {
                    
                    AppLog.info("PlatformHooks - getUserGroupsByAgentTitles add group: " + role.getString(ATT_ROLE_MAPPER_GROUPE), null);
                    
                    userGroups.add(role.getString(ATT_ROLE_MAPPER_GROUPE));
                }
            }
        }
        return userGroups;
    }

    /** Classe décrivant un role enrichi pour Ladom */
    public class LadomRole {

        private String group;

        public String getGroup() {
            return group;
        }

        public void setGroup(String group) {
            this.group = group;
        }
    }
}

```

## Answer
Il y a un traitement qui recharge les droits au logon (avant postLoadGrant), ça pourrait expliquer cette boucle :

Si le scope (la page d'accueil affectée au User) n'est pas renseignée ou qu'elle ne matche pas avec une page d'accueil de ses droits, Simplicité réaffecte automatiquement un scope valide (celle demandée par URL `?_scope=xxx` ou la première autorisée) et recharge les droits pour ce scope valide.

- Avez vous affecté une page d'accueil au User (usr_home_id = row_id de la View) dans votre création/mise à jour du User au preLoadGrant ?
- Si oui fait elle bien partie de ses groupes autorisés ?
