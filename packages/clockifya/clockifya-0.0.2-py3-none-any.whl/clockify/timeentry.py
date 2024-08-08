import logging
logging.basicConfig(level=logging.INFO)
from .abstract_clockify import AbstractClockify
from .user import User
import urllib.parse
from datetime import datetime, timedelta
# Represents time spent on a Task by a User 
class TimeEntry(AbstractClockify):
    
    def __init__(self,api_key):
        super(TimeEntry,self).__init__(api_key=api_key)
	
	# returns all time entry
    def get_all_time_entry_user(self,workspace_id,user_id,last_day=False): 
        try:
            logging.info("Start function: get_all_time_entry_user")
            base_url = self.base_url + 'v1/workspaces/' + workspace_id + '/user/' + user_id + '/time-entries'

            time_entries = []
            page = 1
            has_time_entry = True

            while has_time_entry:
                if last_day:
                    one_day_ago = datetime.utcnow() - timedelta(hours=24)
                    now = datetime.utcnow()
                    start_time = one_day_ago.isoformat() + 'Z'
                    end_time = now.isoformat() + 'Z'
                    url = f"{base_url}?start={urllib.parse.quote(start_time)}&end={urllib.parse.quote(end_time)}&page={page}"
                else:
                    url = f"{base_url}?page={page}"

                r = self.request_get(url)

                if len(r) > 0:
                    time_entries.extend(r)
                    page += 1
                else:
                    has_time_entry = False

            return time_entries	
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)

    def get_by_workspace_function(self, workspace, **kwargs):
        result = []
        time_entries = []
        
        try:
            function = kwargs["function"]

            logging.info("Start function: get_by_workspace_function")

            users = User.get_all_workspace_users(self,workspace['id'])
            for user in users:
                user_id = user['id']
                result = self.get_all_time_entry_user(workspace['id'], user_id,kwargs["last_day"])
                for entry in result:
                    value = entry
                    time_entries.append(value)
                    if function is not None:
                        function (data=value, topic=kwargs["topic"], extra_data=kwargs["extra_data"])
				
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__) 

        logging.info("Retrieve All Time Entries")
        return time_entries

