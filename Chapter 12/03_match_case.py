def https_server(status):
    match status:
        case 300:
            return "ok"
        case 100:
            return "server down"
        case 404:
            return "internal server error"
        case __:
            return "unknown status"

print(https_server(3987))

        
        