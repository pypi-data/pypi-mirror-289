import os
import json

from cc_py_commons.sns.sns_service import SnsService
from cc_py_commons.utils import json_logger

ANALYTICS_SNS_ARN = os.environ.get("ANALYTICS_SNS_ARN")


def send(c4_user_id, c4_account_id, event_type, payload):
	if ANALYTICS_SNS_ARN != "":
		user_data = {'id': c4_user_id, 'accountId': c4_account_id}
		analytics_payload = {**payload, **user_data, 'eventType': event_type}
		json_logger.debug(c4_account_id, 'Sending analytics SNS notification',
						  topic=ANALYTICS_SNS_ARN, event_type=event_type, message=analytics_payload)
		sns_service = SnsService()
		sns_service.send(ANALYTICS_SNS_ARN, analytics_payload.get('subject'), json.dumps(analytics_payload))
		return True

	return False
