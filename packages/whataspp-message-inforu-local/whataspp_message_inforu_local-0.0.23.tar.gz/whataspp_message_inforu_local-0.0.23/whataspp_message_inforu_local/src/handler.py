from logger_local.LoggerLocal import Logger
from python_sdk_local.http_response import handler_decorator
from python_sdk_local.utilities import DEFAULT_LANG_CODE_STR
from message_local.MessageLocal import MessageLocal
from message_local.CompoundMessage import CompoundMessage
from phones_local.phones_local import PhonesLocal
from profile_local.profiles_local import ProfilesLocal

from .WhatsAppLocalConstants import get_logger_object


logger = get_logger_object()


@handler_decorator(logger)
def createHandler(request_parameters: dict) -> dict:
    # In all serverless-com handlers' logger.start()- Add optional parameter
    # to logger.start() which called api_call, so logger.start will call
    # api_management to insert into api_call_table all fields including
    # session_id.
    """Read parameters from the payload and insert them"""

    is_test_data = request_parameters.get("isTestData", False)
    message_data = __extract_message_data(request_parameters)
    message_id = MessageLocal().insert_message_data(message_data=message_data)
    message = {"message": "Message created successfully", "message_id": message_id}
    return message

"""
Example of request_parameters:
{
    "CustomerId":28132,
    "ProjectId":1042593,
    "Data":[
        {
            "Channel":"SMS_MO",
            "Type":"PhoneNumber",
            "Value":"0522222229",
            "Keyword":"wt1",
            "Message":"wt1 ",
            "Network":"WhatsApp",
            "ShortCode":"+97233769182",
            "ApplicationID":"11542",
            "CustomerParam":"SMf14104210035723ecab943567b4ad4b5",
            "MoSessionId":"SMf14104210035723ecab943567b4ad4b5"
        }
    ]
}
"""
def __extract_message_data(request_parameters: dict) -> dict:
    """Extract message data from the payload"""
    phones_local  = PhonesLocal()
    profiles_local = ProfilesLocal()
    message_data = {}
    # message_data["message_type_id"] = request_parameters.get("Type")
    message_data["body"] = request_parameters.get("Message")
    # message_data["message_channel_id"] = request_parameters.get("Channel")
    # message_data["message_network_id"] = request_parameters.get("Network")
    receiver_phone_number = request_parameters.get("ShortCode")
    # message_data["message_application_id"] = request_parameters.get("ApplicationID")
    # message_data["message_customer_param"] = request_parameters.get("CustomerParam")
    # message_data["message_mo_session_id"] = request_parameters.get("MoSessionId")
    # message_data["message_keyword"] = request_parameters.get("Keyword")
    #message_data["sender_phone_number"] = request_parameters.get("Value")
    sender_phone_number = request_parameters.get("Value")
    sender_normalized_phone_number = phones_local.get_normalized_phone_number_by_phone_original_str(sender_phone_number)
    # Replace the leading 0 in the phone number by 972 if there's a leading 0
    if sender_normalized_phone_number.startswith("0"):
        sender_normalized_phone_number = "972" + sender_normalized_phone_number[1:]
    sender_phone_id = phones_local.get_phone_id_by_full_number_normalized(full_number_normalized=sender_normalized_phone_number)
    # Get Sender profile id
    sender_profile_id = profiles_local.select_one_value_by_column_and_value(
        select_clause_value="profile_id", column_name="phone_id", column_value=sender_phone_id
    )
    if sender_profile_id is None:
        # Create and insert a new profile
        profile_dict = {
            "profile.name":  sender_phone_number,
        }
        sender_profile_id = profiles_local.insert(profile_dict=profile_dict)
    message_data["sender_profile_id"] = sender_profile_id
    # Get receiver normalized phone number
    receiver_normalized_phone_number = phones_local.get_normalized_phone_number_by_phone_original_str(receiver_phone_number)
    # Remove leading #
    if receiver_normalized_phone_number.startswith("#"):
        receiver_normalized_phone_number = receiver_normalized_phone_number[1:]

    # Get receiver phone id
    receiver_phone_id = phones_local.get_phone_id_by_full_number_normalized(full_number_normalized=receiver_phone_number)
    # Get receiver profile id
    receiver_profile_id = profiles_local.select_one_value_by_column_and_value(
        select_clause_value="profile_id", column_name="phone_id", column_value=receiver_phone_id
    )
    message_data["to_profile_id"] = receiver_profile_id

    # message_data["message_customer_id"] = request_parameters.get("CustomerId")
    # message_data["message_project_id"] = request_parameters.get("ProjectId")
    return message_data

# TODO: except ValueError as exception, BAD_REQUEST / INTERNAL_SERVER_ERROR...


# @handler_decorator(logger)
# def deleteHandler(request_parameters: dict) -> dict:
#     """url/5   (5 is the eventId)"""

#     message_id = request_parameters.get('eventId')
#     is_test_data = request_parameters.get("isTestData", False)
#     MessageLocal().delete_by_message_id(message_id=message_id)
#     message = {"message": "Message deleted successfully"}
#     return message


# TODO This should be imported from entity-type-python-package (this file will be generated by Sql2Code)
# @handler_decorator(logger)
# def getAllHandler(request_parameters: dict) -> list:
#     """url?langCode=en&limit=10"""

#     lang_code_str = request_parameters.get("langCode") or DEFAULT_LANG_CODE_STR
#     limit = request_parameters.get("limit")
#     is_test_data = request_parameters.get("isTestData", False)
#     messages_list = MessageLocal().select_all_messages(lang_code_str, limit=limit)
#     return messages_list


# @handler_decorator(logger)
# def getMessageByProfileIdHandler(request_parameters: dict) -> list:
#     """url/5?limit=10   (5 is the profileId)"""

#     request_parameters = request_parameters
#     profile_id = request_parameters.get("profileId")
#     limit = request_parameters.get("limit")

#     is_test_data = request_parameters.get("isTestData", False)
#     messages_list = MessageLocal().select_messages_by_profile_id(profile_id, limit=limit)
#     return messages_list


# @handler_decorator(logger)
# def getMessageByeventIdHandler(request_parameters: dict) -> dict:
#     """url/5?isTestData=true   (eventId)"""

#     message_id = request_parameters.get("eventId")

#     is_test_data = request_parameters.get("isTestData", False)
#     message = MessageLocal().select_by_message_id(message_id)
#     if not message:
#         raise Exception(f"Message not found with message_id: {message_id}")
#     return message


# @handler_decorator(logger)
# def updateHandler(request_parameters: dict) -> dict:
#     """url/5  (eventId)
#     Read parameters from the payload and update them"""

#     message_id = request_parameters.get('eventId')
#     is_test_data = request_parameters.get("isTestData", False)
#     if not message_id:
#         raise Exception("message_id is required")

#     MessageLocal().update_by_message_id(message_id, request_parameters)
#     message = {"message": "Message updated successfully"}
#     return message


# @handler_decorator(logger)
# def getMessageByMessageTitleHandler(request_parameters: dict) -> list:  # TODO: test
#     """url/SomeTitle?limit=10"""

#     title = request_parameters.get("title")

#     limit = request_parameters.get("limit")
#     is_test_data = request_parameters.get("isTestData", False)
#     messages_list = MessageLocal().select_events_by_title(title, limit=limit)
#     return messages_list