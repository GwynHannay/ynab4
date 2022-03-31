import dropbox
import configparser

from dropbox import DropboxOAuth2FlowNoRedirect

config = configparser.ConfigParser()
config.read('config/keys.ini')
dropbox_conf = config['DROPBOX']


def get_files_list():
    dbx = dropbox.Dropbox(dropbox_conf['MY_TOKEN'])

    # for entry in dbx.files_list_folder('/YNAB').entries:
    #     print(entry.name)


def connect():
    auth_flow = DropboxOAuth2FlowNoRedirect(
        dropbox_conf['KEY'], dropbox_conf['SECRET'])

    authorize_url = auth_flow.start()
    print("1. Go to: " + authorize_url)
    print("2. Click \"Allow\" (you might have to log in first).")
    print("3. Copy the authorization code.")
    auth_code = input("Enter the authorization code here: ").strip()

    try:
        oauth_result = auth_flow.finish(auth_code)
    except Exception as e:
        print('Error: %s' % (e,))
        exit(1)

    with dropbox.Dropbox(oauth2_access_token=oauth_result.access_token) as dbx:
        dbx.users_get_current_account()
        print("Successfully set up client!")
    
    return dbx


if __name__ == "__main__":
    connect()
