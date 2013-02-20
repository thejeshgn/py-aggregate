#copied from ODK 

# Error message if the form with FORM ID is not found
ODKID_NOT_FOUND = "Unable to find form with matching Form Id as submission"
FORM_NOT_FOUND = "Form not found"
FORM_DEFINITION_INVALID = "Form definition incomplete or missing"
#Error message for if key was not successfully part of the request
ODK_KEY_PROBLEM = "Encountered a problem receiving key"
# Error message if the FORM ID in the form already exists
FORM_WITH_ODKID_EXISTS = "Form Already Exists for this Namespace/Id attribute"

FORM_INVALID_SUBMISSION_ELEMENT = "Attributes of submission element do not match form attributes"
# Error message if not all information was received 
MISSING_FORM_INFO = "Did not receive Form Name and Form XML description"

# Error message if form ID was not specified
MISSING_FORM_ID = "Form did not specify a Form ID. For information on Form ID please check the Open Data Kit FAQ"

# Error message if request is not multi-part 
NO_MULTI_PART_CONTENT = "Request does not contain Multi Part Content"
INCOMPLETE_DATA = "Problem locating part of the submission data needed to complete request"
# Constant error string if child does not implement a setValueFromByteArray override
BINARY_ERROR = "System should have dispatched to a proper binary conversion method"
PARSING_PROBLEM = "Problem parsing submission XML"
FORM_DOES_NOT_ALLOW_SUBMISSIONS = "Submissions have been disallowed on this form"
# Constant used to log error if string array does not match column size
ROW_SIZE_ERROR = "Tried to add a row to result table that did not match the header size! DISCARDING!"
# Error message if not all information was received
INSUFFIECENT_PARAMS = "Insuffiecent Parameters Received"
SUBMISSION_NOT_FOUND ="Did NOT find submission matching the provided parameters"
NO_STRING_TO_BLOB_CONVERT = "Blob cannot be created from string"
UNKNOWN_INTERFACE = "Some how did not get a SubmissionField or SubmissionRepeat"
INVALID_PARAMS = "Parameter(s) are not valid"
MISSING_PARAMS = "One or more required parameters are missing"

# Constant string identifying XML stream
INPUTSTREAM_ERROR = "Problem obtaining submissionXML input stream!"
NO_IMAGE_EXISTS = "No Image Exists for this Entry!"
NOT_A_KEY = "Incorrect type was stored, expecting a key for the view link"
TASK_PROBLEM = "PROBLEM WITH TASK: "

QUOTA_EXCEEDED = "Quota exceeded"
PERSISTENCE_LAYER_PROBLEM = "Problem persisting data or accessing data"
UPLOAD_PROBLEM = "Upload transmission unexpectedly failed"
EXPORTED_FILE_PROBLEM = "Problem accessing exported datafile"

JAVA_ROSA_PARSING_PROBLEM = "Problem with JavaRosa Parsing Form:"
ERROR_OBTAINING_FUSION_TABLE_ID = "ERROR CREATING FUSION TABLE - DID NOT GET A TABLE NUMBER"

# Error message if OAuth authentication failed.
OAUTH_ERROR = "OAuth authentication failed."
OAUTH_SECURITY_ERROR_WHILE_RETRIEVING_SESSION_TOKEN = "Security error while retrieving session token."
OAUTH_SERVER_REJECTED_ONE_TIME_USE_TOKEN = "Server rejected one time use token."