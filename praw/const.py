"""praw constants."""

__version__ = '4.0.0b20'

API_PATH = {
    'accept_mod_invite':      'api/accept_moderator_invite',
    'access_token_url':       'api/v1/access_token/',
    'approve':                'api/approve/',
    'authorize':              'api/v1/authorize/',
    'banned':                 'r/{subreddit}/about/banned/',
    'block':                  'api/block',
    'blocked':                'prefs/blocked/',
    'by_id':                  'by_id/',
    'captcha':                'captcha/',
    'collapse_message':       'api/collapse_message/',
    'comment':                'api/comment/',
    'comment_replies':        'message/comments/',
    'comments':               'comments/',
    'compose':                'api/compose/',
    'contest_mode':           'api/set_contest_mode/',
    'contributor':            'r/{subreddit}/about/contributors/',
    'controversial':          'controversial/',
    'del':                    'api/del/',
    'deleteflair':            'api/deleteflair',
    'delete_redditor':        'api/delete_user',
    'delete_sr_header':       'r/{subreddit}/api/delete_sr_header',
    'delete_sr_image':        'r/{subreddit}/api/delete_sr_img',
    'distinguish':            'api/distinguish/',
    'domain':                 'domain/{domain}/',
    'duplicates':             'duplicates/{submission_id}/',
    'edit':                   'api/editusertext/',
    'edited':                 'r/{subreddit}/about/edited/',
    'flair':                  'r/{subreddit}/api/flair/',
    'flairconfig':            'api/flairconfig/',
    'flaircsv':               'r/{subreddit}/api/flaircsv/',
    'flairlist':              'r/{subreddit}/api/flairlist/',
    'flairselector':          'r/{subreddit}/api/flairselector/',
    'flairtemplate':          'r/{subreddit}/api/flairtemplate/',
    'flairtemplateclear':     'r/{subreddit}/api/clearflairtemplates/',
    'flairtemplatedelete':    'r/{subreddit}/api/deleteflairtemplate/',
    'friend':                 'api/friend/',
    'friend_v1':              'api/v1/me/friends/{user}',
    'friends':                'api/v1/me/friends/',
    'gild_thing':             'api/v1/gold/gild/{fullname}/',
    'gild_user':              'api/v1/gold/give/{username}/',
    'help':                   'help/',
    'hide':                   'api/hide/',
    'ignore_reports':         'api/ignore_reports/',
    'inbox':                  'message/inbox/',
    'info':                   'api/info/',
    'karma':                  'api/v1/me/karma',
    'leavecontributor':       'api/leavecontributor',
    'leavemoderator':         'api/leavemoderator',
    'liveabout':              'api/live/{id}/about/',
    'livecreate':             'api/live/create',
    'lock':                   'api/lock/',
    'me':                     'api/v1/me',
    'mentions':               'message/mentions',
    'message':                'message/messages/{messageid}/',
    'messages':               'message/messages/',
    'moderator':              'r/{subreddit}/about/moderators/',
    'moderator_messages':     'r/{subreddit}/message/moderator/',
    'moderator_unread':       'r/{subreddit}/message/moderator/unread/',
    'modlog':                 'r/{subreddit}/about/log/',
    'modqueue':               'r/{subreddit}/about/modqueue/',
    'morechildren':           'api/morechildren/',
    'my_contributor':         'subreddits/mine/contributor/',
    'my_moderator':           'subreddits/mine/moderator/',
    'my_multireddits':        'api/multi/mine/',
    'my_subreddits':          'subreddits/mine/subscriber/',
    'new':                    'new/',
    'marknsfw':               'api/marknsfw/',
    'multireddit':            'user/{user}/m/{multi}/',
    'multireddit_api':        'api/multi/user/{user}/m/{multi}/',
    'multireddit_base':       'api/multi/',
    'multireddit_copy':       'api/multi/copy/',
    'multireddit_rename':     'api/multi/rename/',
    'multireddit_update':     'api/multi/user/{user}/m/{multi}/r/{subreddit}',
    'multireddit_user':       'api/multi/user/{user}/',
    'mute_sender':            'api/mute_message_author/',
    'muted':                  'r/{subreddit}/about/muted/',
    'read_message':           'api/read_message/',
    'reddit_url':             '/',
    'register':               'api/register/',
    'remove':                 'api/remove/',
    'report':                 'api/report/',
    'reports':                'r/{subreddit}/about/reports/',
    'rising':                 'rising/',
    'save':                   'api/save/',
    'saved':                  'saved/',
    'search':                 'r/{subreddit}/search/',
    'select_flair':           'r/{subreddit}/api/selectflair/',
    'sent':                   'message/sent/',
    'sticky':                 'r/{subreddit}/about/sticky/',
    'sticky_submission':      'api/set_subreddit_sticky/',
    'site_admin':             'api/site_admin/',
    'spam':                   'r/{subreddit}/about/spam/',
    'stylesheet':             'r/{subreddit}/about/stylesheet/',
    'sub_recommendations':    'api/recommend/sr/{subreddits}',
    'submission':             'comments/{id}/',
    'submission_replies':     'message/selfreply/',
    'submit':                 'api/submit/',
    'subreddit':              'r/{subreddit}/',
    'subreddit_about':        'r/{subreddit}/about/',
    'subreddit_comments':     'r/{subreddit}/comments/',
    'subreddit_css':          'api/subreddit_stylesheet/',
    'subreddit_random':       'r/{subreddit}/random/',
    'subreddit_settings':     'r/{subreddit}/about/edit/',
    'subreddit_traffic':      'r/{subreddit}/about/traffic/',
    'subreddits_default':     'subreddits/default/',
    'subreddits_gold':        'subreddits/gold/',
    'subreddits_new':         'subreddits/new/',
    'subreddits_popular':     'subreddits/popular/',
    'subreddits_name_search': 'api/search_reddit_names/',
    'subreddits_search':      'subreddits/search/',
    'subscribe':              'api/subscribe/',
    'suggested_sort':         'api/set_suggested_sort/',
    'top':                    'top/',
    'uncollapse_message':     'api/uncollapse_message/',
    'unfriend':               'api/unfriend/',
    'unhide':                 'api/unhide/',
    'unignore_reports':       'api/unignore_reports/',
    'unlock':                 'api/unlock/',
    'unmarknsfw':             'api/unmarknsfw/',
    'unmoderated':            'r/{subreddit}/about/unmoderated/',
    'unmute_sender':          'api/unmute_message_author/',
    'unread':                 'message/unread/',
    'unread_message':         'api/unread_message/',
    'unsave':                 'api/unsave/',
    'upload_image':           'api/upload_sr_img',
    'user':                   'user/{user}/',
    'user_about':             'user/{user}/about/',
    'username_available':     'api/username_available/',
    'vote':                   'api/vote/',
    'wiki_edit':              'r/{subreddit}/api/wiki/edit/',
    'wiki_page':              'r/{subreddit}/wiki/{page}',
    'wiki_page_editor':       'r/{subreddit}/api/wiki/alloweditor/{method}',
    'wiki_page_settings':     'r/{subreddit}/wiki/settings/{page}',
    'wiki_pages':             'r/{subreddit}/wiki/pages/',
    'wikibanned':             'r/{subreddit}/about/wikibanned/',
    'wikicontributor':        'r/{subreddit}/about/wikicontributors/'}

JPEG_HEADER = b'\xff\xd8\xff'
MAX_IMAGE_SIZE = 512000
MIN_PNG_SIZE = 67
MIN_JPEG_SIZE = 128
PNG_HEADER = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'

USER_AGENT_FORMAT = '{{}} PRAW/{}'.format(__version__)
