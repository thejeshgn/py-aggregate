#copied from ODK 


DEBUG = false

APPLICATION_NAME = "ODK AGGREGATE"
OPEN_ROSA_VERSION_HEADER = "X-OpenRosa-Version"
OPEN_ROSA_VERSION = "1.0"
OPEN_ROSA_DATE_HEADER = "Date"
OPEN_ROSA_ACCEPT_CONTENT_LENGTH_HEADER = "X-OpenRosa-Accept-Content-Length"

#Flag on submissions and form uploads indicating that this is 
#a partial submission or form upload.
TRANSFER_IS_INCOMPLETE = "*isIncomplete*"
#Name of form field that contains XML submission
XML_SUBMISSION_FILE = "xml_submission_file"
#Name of form field that contains the form name value (form upload)
public final static String FORM_NAME_PRAM = "form_name"
# Name of form field that contains the xform xml definittion (form upload)
public final static String FORM_DEF_PRAM = "form_def_file"
#The name of the property that includes the form id
FORM_ID = "formId"

# For PersistentResults and MiscTasks generator gae servlets.
# the key holding the Uri of the persistent result or misc task record.
PERSISTENT_RESULTS_KEY = "persistentResult"
MISC_TASKS_KEY = "miscTask"
ATTEMPT_COUNT = "attemptCount"
BACKEND_GAE_SERVICE = "background"
HOST = "Host"

#The name of the property that determines how to format webpage
HUMAN_READABLE = "readable"

# The name of the property that specifies the type of interaction with an
# external service
EXTERNAL_SERVICE_TYPE = "externalServiceType"

# href link text
BRIEFCASE_LINK_TEXT = "Download Entire Dataset (Briefcase)"
UPLOAD_SUBMISSIONS_LINK_TEXT = "Upload Submissons"
UPLOAD_XFORM_LINK_TEXT = "Upload a Form Definition"
BLOB_KEY = "blobKey"
AS_ATTACHMENT = "as_attachment"
OAUTH_CONSUMER_KEY = "anonymous"
OAUTH_CONSUMER_SECRET = "anonymous"
OAUTH_TOKEN_PARAMETER = "oauth_token"
OAUTH_TOKEN_SECRET_PARAMETER = "oauth_token_secret"
DOWNLOAD_XML_BUTTON_TXT = "Download XML"
CSV_FILENAME_APPEND = "_results.csv"
KML_FILENAME_APPEND = "_results.kml"
JSON_FILENAME_APPEND = "_results.json"
RECORD_KEY = "record"
EXPORT_CURSOR_CHUNK_SIZE = 100

#The name of the parameter that specifies the cursor location for retrieving
# data from the data table (fragmented Csv servlet)
CURSOR = "cursor"
# The name of the parameter that specifies how many rows to return from the
# cursor (fragmented Csv servlet).
NUM_ENTRIES = "numEntries"
CHECK_INTERVAL_PARAM = "checkIntervalMilliseconds"
START_DATE = "startDate"

# Script path to include...
UPLOAD_SCRIPT_RESOURCE = "javascript/upload_control.js"
UPLOAD_STYLE_RESOURCE = "stylesheets/upload.css"
UPLOAD_BUTTON_STYLE_RESOURCE = "stylesheets/button.css"
AGGREGATE_STYLE = "AggregateUI.css"