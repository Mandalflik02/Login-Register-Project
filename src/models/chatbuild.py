


CLIENT_COMMENDS={
	"login":{
		"cmd":"LOGIN",
		"code":73
	},
	"logout": {
		"cmd": "LOGOUT",
		"code": 11
	},
	"message":{
		"cmd":"MSG",
		"code":45
	}
}

SERVER_COMMENDS={
	"login_ok":{
		"cmd":"LOGIN_OK",
		"code":37
	},
	"login_not_ok": {
		"cmd": "LOGIN_NOT_OK",
		"code": 36
	},
	"new_message":{
		"cmd":"NEW_MSG",
		"code":54
	}
}




def build_msg(cmd,code,data_list):
	data=build_data(data_list)
	msg=cmd+"?"+str(code)+"?"+data
	return msg


def build_data(data_list):
	data=""
	for d in data_list:
		data+=d+"|"
	return data[0:-1]