from fastapi                            import Security, Request, Depends
from fastapi.security                   import APIKeyHeader
from osbot_fast_api.api.Fast_API_Routes import Fast_API_Routes

from cbr_athena.odin.Odin__CBR__User_Session import Odin__CBR__User_Session
from osbot_utils.base_classes.Type_Safe import Type_Safe
from osbot_utils.utils.Objects import obj_data

ROUTE_PATH__USER_SESSION        = 'user-session'
EXPECTED_ROUTES__USER_SESSION   = ['/session-details']

api_key_header   = APIKeyHeader(name="Authorization", auto_error=False)

class CBR__Session_Auth(Type_Safe):
    odin_cbr_user_session : Odin__CBR__User_Session

    def session_id_to_session_data(self,  request: Request, session_id: str = Security(api_key_header)):
        if session_id is None:
            if 'CBR__TOKEN' in request.cookies:
                session_id = request.cookies.get('CBR__TOKEN')
        session_data = self.odin_cbr_user_session.user_session_data(session_id)
        return session_data


cbr_session_auth = CBR__Session_Auth()

class Routes__User_Session(Fast_API_Routes):

    tag : str = ROUTE_PATH__USER_SESSION

    def session_details(self, session_data: str = Depends(cbr_session_auth.session_id_to_session_data)):
        return { 'session_details': session_data}

    def setup_routes(self):
        self.add_route_get(self.session_details)