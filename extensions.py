def main():
    f_name = input("File name: ")

    f_name = f_name.strip()
    f_name = f_name.lower()
    suffix = f_name.split(".")[-1]

    dict_mediatypes = {"gif" : "image/gif", "jpg":"image/jpeg", "jpeg":"image/jpeg", "png":"image/png", "pdf":"application/pdf","txt":"text/plain","zip":"application/zip"}

    if f_name.endswith((".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip")):
        for mediatype in dict_mediatypes:
            if mediatype == suffix:
                print(dict_mediatypes[mediatype])

    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()
