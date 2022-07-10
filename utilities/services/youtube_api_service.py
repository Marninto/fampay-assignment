import traceback

import requests
from django.conf import settings

from utilities.constants import MAX_RESULTS

# link = 'https://www.googleapis.com/youtube/v3/search/'
# key = 'AIzaSyAmKQLI3GvT5MYkPSwBjiHakL4e5UIYi9c'


class YoutubeService:
    @classmethod
    def fetch_search_data(cls, query, key, page_token=''):
        try:
            # todo figure out etag api call for optimization
            resp = requests.get(url=f'{settings.GOOGLE_API_BASE_URL}youtube/v3/search/', params={
                "part": 'snippet',
                "maxResults": MAX_RESULTS,
                "q": query,
                "key": key,
                "pageToken": page_token,
                "order": "date",
            })
            if resp.status_code == 200:
                return {'success': True, 'data': resp.json()}
            elif resp.status_code == 429:
                return {'success': True, 'data': None}
            else:
                return {'success': False, 'data': None}
        except Exception:
            tb = traceback.format_exc()
            print(tb)
            # ideally add a logger here
            return {'success': False, 'data': None}

mock_resp = {
  'kind': 'youtube#searchListResponse',
  'etag': 'gwjlc0YX6Bbg8eesj7cFRXp6AIc',
  'nextPageToken': 'CDIQAA',
  'regionCode': 'IN',
  'pageInfo': {
    'totalResults': 1000000,
    'resultsPerPage': 50
  },
  'items': [
    {
      'kind': 'youtube#searchResult',
      'etag': 'zYnECCVzzkHk4ZWHPi_QTTHc8bA',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'QXhV148EryQ'
      },
      'snippet': {
        'publishedAt': '2021-04-09T16:45:01Z',
        'channelId': 'UC9j-24zF2RK7obcSPrSd7Lg',
        'title': 'The Day Cristiano Ronaldo Taught Football to Neymar &amp; Mbappe',
        'description': 'SUBSCRIBE AND TURN ON YOUR ON YOUR NOTIFICATIONS! FOLLOW ME ON: TikTok: https://www.tiktok.com/@alsidofootball ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/QXhV148EryQ/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/QXhV148EryQ/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/QXhV148EryQ/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Alsido Football',
        'liveBroadcastContent': 'none',
        'publishTime': '2021-04-09T16:45:01Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'pyH9YWO9tfuv-ye0LvVFaWTpK78',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'O74Len3wKN8'
      },
      'snippet': {
        'publishedAt': '2022-07-09T01:00:06Z',
        'channelId': 'UCBQkl-NzfkP8uOrlQ3LEwzg',
        'title': 'FUNNY PENALTY KICK ! RJ SPORTING VS NIRMAL BRO&#39;S  ! HARMU FOOTBALL TOURNAMENT JHARKHAND 2022 !',
        'description': "RJ SPORTING WON ON PENALTIES THIS IS THE BEST PENALTY SHOOTOUT ! RJ SPORTING VS NIRMAL BRO'S ! HARMU ...",
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/O74Len3wKN8/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/O74Len3wKN8/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/O74Len3wKN8/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Bindas Football',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-07-09T01:00:06Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': '3WLvp5DrR5HafF6XcjFVkkyNvME',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'vTVuB1kgpd4'
      },
      'snippet': {
        'publishedAt': '2022-01-14T12:39:04Z',
        'channelId': 'UC9j-24zF2RK7obcSPrSd7Lg',
        'title': '32 Legendary Goals in Football History',
        'description': 'SUBSCRIBE AND TURN ON YOUR ON YOUR NOTIFICATIONS! FOLLOW ME ON: TikTok: https://www.tiktok.com/@alssido ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/vTVuB1kgpd4/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/vTVuB1kgpd4/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/vTVuB1kgpd4/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Alsido Football',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-01-14T12:39:04Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'HW4-8iFTH8_vOHAgUzxeXkq57Sk',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'HZHteaZIAl4'
      },
      'snippet': {
        'publishedAt': '2021-10-20T09:15:57Z',
        'channelId': 'UC6TiDPJ5fDo0iI2X9nkp6FQ',
        'title': 'Cristiano ronaldo whatsapp status|football |#shorts #cristianoronaldo #football #CR7VERIYAN ᴄʟɪᴄᴋ👇',
        'description': 'cr7#cristianoronaldo#football#shorts.',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/HZHteaZIAl4/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/HZHteaZIAl4/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/HZHteaZIAl4/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'CR7 VERIYAN',
        'liveBroadcastContent': 'none',
        'publishTime': '2021-10-20T09:15:57Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'bFSIc6al856LxSTt_q2JYkceA_M',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'HL8Er3cP2b4'
      },
      'snippet': {
        'publishedAt': '2022-02-03T13:53:47Z',
        'channelId': 'UCwX2idbM0VPJCbEcWU9aw_w',
        'title': '1 in a Trillion Football Moments',
        'description': '1 in a Trillion Moments in Football ➣ Instagram: https://goo.gl/S9QEjJ ➣ twitter: https://goo.gl/rQHspX Music: ᐉ Royalty-Free ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/HL8Er3cP2b4/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/HL8Er3cP2b4/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/HL8Er3cP2b4/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Xiimo',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-02-03T13:53:47Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'I85GXX8dDdh2n21_3CQCF1EVSdA',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'BYp2RriTqGc'
      },
      'snippet': {
        'publishedAt': '2022-04-19T11:32:08Z',
        'channelId': 'UCMm6vrmAdq4H5r6pi0csuWQ',
        'title': 'Unforgettable Goals In Football ● Football Greatest Moments',
        'description': 'Unforgettable Goals In Football ○ Football Greatest Moments Infraction - Action ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/BYp2RriTqGc/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/BYp2RriTqGc/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/BYp2RriTqGc/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'GrdArena',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-04-19T11:32:08Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'nYUMdu_anJbFQ473lFSJQrXrbSQ',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'iLwx2HtJhA8'
      },
      'snippet': {
        'publishedAt': '2022-07-08T23:04:40Z',
        'channelId': 'UCU2PacFf99vhb3hNiYDmxww',
        'title': 'Chelsea Men return to pre-season training! ☀️ | Chelsea Unseen',
        'description': 'Ahead of their 2022 U.S. Pre-Season Tour, Chelsea Men returned to full training at sunny Cobham Training Centre. Watch the ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/iLwx2HtJhA8/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/iLwx2HtJhA8/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/iLwx2HtJhA8/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Chelsea Football Club',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-07-08T23:04:40Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'fL9xDT05D4sTY7t4yRgpX6yFAu0',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'YW9e3BlcTKs'
      },
      'snippet': {
        'publishedAt': '2022-07-08T08:31:19Z',
        'channelId': 'UCpryVRk_VDudG8SHXgWcG0w',
        'title': 'Pre-season training in Germany | Inside Training',
        'description': 'The squad are hard at work in Germany, where they train at adidas HQ. #arsenal #gabrieljesus #mikelarteta Enjoy match ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/YW9e3BlcTKs/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/YW9e3BlcTKs/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/YW9e3BlcTKs/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Arsenal',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-07-08T08:31:19Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'jJRmX3ytzmFCVVPk4b9XT7qUBy0',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'qh-yxk-qAOc'
      },
      'snippet': {
        'publishedAt': '2021-03-19T10:00:27Z',
        'channelId': 'UCSpvzqzfRAJGAWcuYjxWRbw',
        'title': 'Unforgettable Goals in Football #2',
        'description': 'Unforgettable and best goals in football. Messi, Ronaldo, Ibrahimovic, Rashford and more in the video! Infraction - Cold Harbour ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/qh-yxk-qAOc/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/qh-yxk-qAOc/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/qh-yxk-qAOc/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'TKHD',
        'liveBroadcastContent': 'none',
        'publishTime': '2021-03-19T10:00:27Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': '83G_rQGX9yWDfwBdvZ8H0gJ8w2s',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'O-H9PyNckeQ'
      },
      'snippet': {
        'publishedAt': '2022-04-29T08:49:20Z',
        'channelId': 'UCMm6vrmAdq4H5r6pi0csuWQ',
        'title': 'Greatest World Record In Football',
        'description': 'Greatest World Record In Football Infraction - Gemini https://youtu.be/vNarBb07SKM Infraction - Colors ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/O-H9PyNckeQ/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/O-H9PyNckeQ/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/O-H9PyNckeQ/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'GrdArena',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-04-29T08:49:20Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': '0yTFkwWaQPvnJ9wNRE_0RK_fkhk',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'DtGlCClazLc'
      },
      'snippet': {
        'publishedAt': '2022-07-08T18:00:11Z',
        'channelId': 'UCcw05gGzjLIs5dnxGkQHMvw',
        'title': 'The latest on transfers from Spain: Frenkie de Jong, Robert Lewandowski and more',
        'description': 'Subscribe to Sky Sports News: http://bit.ly/SkySportsNewsSub Spanish football jourmalist Alvaro Montero provides the latest on ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/DtGlCClazLc/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/DtGlCClazLc/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/DtGlCClazLc/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Sky Sports News',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-07-08T18:00:11Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'HIK2n_ie-UbCbTPuHE62dAJ41b8',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'ADynE-DQLr4'
      },
      'snippet': {
        'publishedAt': '2022-03-24T09:34:13Z',
        'channelId': 'UCvJywWV7q0hTKIRVxSHAs7A',
        'title': '1 in a Trillion Moments in Football History',
        'description': '1 in a Trillion moments in football History. In this video you can see epic rare moments in football. You can also see top moments ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/ADynE-DQLr4/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/ADynE-DQLr4/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/ADynE-DQLr4/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'NV10HD',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-03-24T09:34:13Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'Pby7rSjPjSvDh5tfISTHprU88dU',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'vwtUVwXWy8Y'
      },
      'snippet': {
        'publishedAt': '2020-12-12T16:13:17Z',
        'channelId': 'UCFz1irDsvD3_8H-hzk-Fytg',
        'title': 'KIDS IN FOOTBALL - FAILS, SKILLS &amp; GOALS #1',
        'description': 'In this video you will see kids / children scoring amazing goals, making hilarious fails and doing the most crazy skills in football.',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/vwtUVwXWy8Y/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/vwtUVwXWy8Y/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/vwtUVwXWy8Y/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'SKILLER',
        'liveBroadcastContent': 'none',
        'publishTime': '2020-12-12T16:13:17Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'A3SvFuBO6kRUkOTTQFLmmsa5LFw',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'URlA02MPXu0'
      },
      'snippet': {
        'publishedAt': '2022-07-09T11:53:08Z',
        'channelId': 'UCjJeMQLzfzkfIHvTHKoJ4qg',
        'title': 'Vaivakawn LC vs Champhai Kanan VC | All Mizoram Inter Village Football Tournament | AR GROUND | LIVE',
        'description': 'The official youtube channel of Zonet Cable TV Pvt. Ltd. Follow us: Instagram : https://www.instagram.com/zonet_official/ ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/URlA02MPXu0/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/URlA02MPXu0/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/URlA02MPXu0/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Zonet',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-07-09T11:53:08Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'VnHbUkI7k6yhSGZjXHbxFmDK_qo',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'z7WzDlanZmg'
      },
      'snippet': {
        'publishedAt': '2022-04-08T10:00:10Z',
        'channelId': 'UC740ilqsaYlnp0CFdYQoowA',
        'title': 'Revenge Moments in Football',
        'description': 'Revenge Moments in Football TURN NOTIFICATIONS ON   https://www.instagram.com/player.3r.',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/z7WzDlanZmg/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/z7WzDlanZmg/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/z7WzDlanZmg/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Teo CRi',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-04-08T10:00:10Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'EpGZfGsOjjqf-qEigjgAbvX9HJw',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'lG5fBDsSixM'
      },
      'snippet': {
        'publishedAt': '2022-04-14T17:38:05Z',
        'channelId': 'UCU6JLYuerEUb7VrDd4zLihg',
        'title': 'Moments that Can&#39;t be Repeated in Football',
        'description': "Moments that Can't be Repeated in Football IF YOU LIKE SOCCER JOIN THE CHANNEL: https://goo.gl/bhZX1O #football ...",
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/lG5fBDsSixM/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/lG5fBDsSixM/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/lG5fBDsSixM/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'SportsHD',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-04-14T17:38:05Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'fpdlcEN3BYIOAbv9sX8v9uAdsYY',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'ZEBVQ2Y0QiU'
      },
      'snippet': {
        'publishedAt': '2022-03-02T10:38:31Z',
        'channelId': 'UCX7NrBIGUezEJxDK3vCZa7Q',
        'title': 'Comedy Moments in Football',
        'description': 'Follow us! • Instagram - https://instagram.com/score90 • TikTok - https://tiktok.com/@score90 Score 90 is a Swedish brand, ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/ZEBVQ2Y0QiU/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/ZEBVQ2Y0QiU/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/ZEBVQ2Y0QiU/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Score 90',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-03-02T10:38:31Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'IniOIaSTSEqJ9wlr2qhCHofRyVI',
      'id': {
        'kind': 'youtube#video',
        'videoId': '_Mht_TiUBPs'
      },
      'snippet': {
        'publishedAt': '2022-06-13T12:02:21Z',
        'channelId': 'UCj4OE3L5OVEphzpTRmGTtAQ',
        'title': 'Revenge Moments in Football',
        'description': '30.000 LIKES ON " Revenge Moments "? - Clarx - Zig Zag [NCS Release] ---- https://youtu.be/CLEWmT_8ppM - Epic ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/_Mht_TiUBPs/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/_Mht_TiUBPs/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/_Mht_TiUBPs/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Soccer90v',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-06-13T12:02:21Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'nx2mClSmSv18xomTtRjGQeV89c4',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'z7xI58dFZjI'
      },
      'snippet': {
        'publishedAt': '2019-04-25T01:58:44Z',
        'channelId': 'UCjrLVNjIdMwBDU22NqRMJ4A',
        'title': 'Best Animated Football Ads ft Messi &amp; Ronaldo.',
        'description': 'Ads#Messi#Ronaldo.',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/z7xI58dFZjI/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/z7xI58dFZjI/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/z7xI58dFZjI/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'FootVic',
        'liveBroadcastContent': 'none',
        'publishTime': '2019-04-25T01:58:44Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'vIkjTScXIgSg7o41FU9R41IKTc8',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'GcV9vI2mX2c'
      },
      'snippet': {
        'publishedAt': '2022-06-19T11:00:06Z',
        'channelId': 'UC740ilqsaYlnp0CFdYQoowA',
        'title': 'Most Satisfying Goals in Football',
        'description': 'Most Satisfying Goals in Football TURN NOTIFICATIONS ON   https://www.instagram.com/player.3r.',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/GcV9vI2mX2c/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/GcV9vI2mX2c/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/GcV9vI2mX2c/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Teo CRi',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-06-19T11:00:06Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 's1R35PU78NG3TsKXBKGqQrSerkA',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'EMDphB1GiU8'
      },
      'snippet': {
        'publishedAt': '2022-06-03T10:12:52Z',
        'channelId': 'UClvgyQvIplPQU8N73vPlFUA',
        'title': '1 in a Billion Moments',
        'description': 'TURN ON NOTIFICATIONS TO NEVER MISS AN UPLOAD!   Twitter: https://twitter.com/ashstudio7 Instagram: ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/EMDphB1GiU8/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/EMDphB1GiU8/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/EMDphB1GiU8/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'AshStudio7',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-06-03T10:12:52Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'nPG2pUHvfo-PuGcaAE17mTplmV8',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'NtLntbuBw4I'
      },
      'snippet': {
        'publishedAt': '2022-07-08T13:30:07Z',
        'channelId': 'UC-BlL1ERev9O82Ar4WQmKig',
        'title': 'Shocking Football Chats That You Missed',
        'description': "The most shocking & funny chats you've probably seen in Football. All from Cristiano Ronaldo, Messi, Neymar any many more!",
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/NtLntbuBw4I/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/NtLntbuBw4I/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/NtLntbuBw4I/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'FOOT4K',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-07-08T13:30:07Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'RT8N4U6qX1cWl3a4j4qUnWcfNbY',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'BzNMJILF0ok'
      },
      'snippet': {
        'publishedAt': '2022-05-21T15:30:00Z',
        'channelId': 'UCaRWArjOtQAHHe2C7B4m8Uw',
        'title': 'Goals that Can&#39;t be Repeated in Football',
        'description': "Goals that Can't be Repeated in Football Watch in this video the most humiliating and legendary goals in football. : ThimLife ...",
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/BzNMJILF0ok/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/BzNMJILF0ok/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/BzNMJILF0ok/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'iLance7i',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-05-21T15:30:00Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': '0Pakp4iGUxTt59EnuIxi9mL9EqA',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'D7kJFEAYBOk'
      },
      'snippet': {
        'publishedAt': '2022-01-17T14:30:02Z',
        'channelId': 'UC-BlL1ERev9O82Ar4WQmKig',
        'title': 'Football | 0% Luck ,100% Talent',
        'description': 'Watch talents playing Football IF YOU LIKE THIS VIDEO JOIN THE CHANNEL: https://bit.ly/3ddpLcC Music: My Lord - Song by ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/D7kJFEAYBOk/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/D7kJFEAYBOk/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/D7kJFEAYBOk/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'FOOT4K',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-01-17T14:30:02Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'A4BsZdt8JnWSKtdC8ut5iTg5RlY',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'BJdR8wPVk_4'
      },
      'snippet': {
        'publishedAt': '2022-06-16T12:13:29Z',
        'channelId': 'UCkSPtBTMu2_hht6uz5euWUQ',
        'title': 'Impossible Moments In Football',
        'description': 'Impossible Moments In Football If You Like Football Please Join The Channel:https://www.youtube.com/c/No10player ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/BJdR8wPVk_4/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/BJdR8wPVk_4/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/BJdR8wPVk_4/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'No.10 player',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-06-16T12:13:29Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'PnbuDlwmTZayyZUIYXeSnw3cbRA',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'b_qEUyvPdN8'
      },
      'snippet': {
        'publishedAt': '2022-07-08T20:15:01Z',
        'channelId': 'UCeggrzoAahf4hhSB1hgYHBA',
        'title': 'FIFA 22 | NEW CONFIRMED TRANSFERS &amp; RUMOURS! 🤯😱 | FT. Dybala, Ronaldo, Di María...',
        'description': 'This video is about latest transfers. In this video you can find information about latest football transfers. Which player could left his ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/b_qEUyvPdN8/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/b_qEUyvPdN8/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/b_qEUyvPdN8/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Dervaoo',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-07-08T20:15:01Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'RB3lq8v2pQYAZCm0aJvhQcdVcYo',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'p_Fiqoe4tA8'
      },
      'snippet': {
        'publishedAt': '2022-06-13T09:56:55Z',
        'channelId': 'UClvgyQvIplPQU8N73vPlFUA',
        'title': 'Embarrassing Moments',
        'description': 'TURN ON NOTIFICATIONS TO NEVER MISS AN UPLOAD!   Twitter: https://twitter.com/ashstudio7 Instagram: ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/p_Fiqoe4tA8/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/p_Fiqoe4tA8/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/p_Fiqoe4tA8/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'AshStudio7',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-06-13T09:56:55Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'eTUNXqbJtvjzAqEO_eFWpSQqmSI',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'y8H9AOf413M'
      },
      'snippet': {
        'publishedAt': '2022-01-29T06:30:21Z',
        'channelId': 'UCXsJyNCjFthPLQ9U5KI-Frg',
        'title': '20 CRAZIEST Goals In Football History',
        'description': 'These are the 20 CRAZIEST Goals in Football History.. Follow Our Social Media: Tik Tok: @thekickflix Instagram: ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/y8H9AOf413M/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/y8H9AOf413M/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/y8H9AOf413M/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'KickFlix',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-01-29T06:30:21Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'KhmU6CJWHVXGYP-LsFjG91VK9_U',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'fDvUbpOe0xQ'
      },
      'snippet': {
        'publishedAt': '2022-07-09T09:18:33Z',
        'channelId': 'UCGfkjaC7xPik892a1LeQULA',
        'title': 'Why This Could Be The PERFECT Transfer Window For Thomas Tuchel!',
        'description': "Why This Could Be The PERFECT Transfer Window For Thomas Tuchel! Thomas Tuchel is the driving force behind Chelsea's ...",
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/fDvUbpOe0xQ/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/fDvUbpOe0xQ/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/fDvUbpOe0xQ/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Football Therapy',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-07-09T09:18:33Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'rsbidRcr_tEHkq3wMrp1boUecMY',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'VzVIPp83Ses'
      },
      'snippet': {
        'publishedAt': '2022-02-03T14:20:33Z',
        'channelId': 'UCJ-_I0557MXQsSk1Jo1Hj0w',
        'title': 'Football Games Worth Watching Again - 2021/22 #5',
        'description': 'This is the fifth part of one of my favorite series to create. There are some amazing games in this video you should definitely see.',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/VzVIPp83Ses/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/VzVIPp83Ses/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/VzVIPp83Ses/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Vanemas Football',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-02-03T14:20:33Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'Oinn-xXYkdHTh_ILTfZW_tNfR_w',
      'id': {
        'kind': 'youtube#video',
        'videoId': '7hyt0ClX6Oo'
      },
      'snippet': {
        'publishedAt': '2022-02-04T19:00:03Z',
        'channelId': 'UCOo_v3eVbfET7_zi2KLOP9g',
        'title': 'Shaolin Soccer Most Epic Scenes',
        'description': 'If football and kung fu had a baby it would be Shaolin Soccer ⚽   BINGE MORE: https://youtu.be/esCTSMkj6OE 00:00 #6 01:51 ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/7hyt0ClX6Oo/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/7hyt0ClX6Oo/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/7hyt0ClX6Oo/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Binge Society ',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-02-04T19:00:03Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'F_mTkQKsBNBWsliwP8Ddm7Zu86c',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'Idido_mcHm0'
      },
      'snippet': {
        'publishedAt': '2019-06-01T08:59:00Z',
        'channelId': 'UCB_l9j53BhS-UNxXO4y282A',
        'title': 'Football in India | Funcho',
        'description': 'The big bonuses are here‼ Hurry to to win easy money in casino and cases✓ https://bit.ly/31Udhze Do you want to win big money ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/Idido_mcHm0/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/Idido_mcHm0/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/Idido_mcHm0/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Funcho',
        'liveBroadcastContent': 'none',
        'publishTime': '2019-06-01T08:59:00Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'k8oO85g2Z8qyjE9YedUJezKw1II',
      'id': {
        'kind': 'youtube#video',
        'videoId': '6M2Zgr6SnHQ'
      },
      'snippet': {
        'publishedAt': '2022-07-07T16:10:12Z',
        'channelId': 'UCNAf1k0yIjyGu3k9BwAg3lg',
        'title': 'What&#39;s next for Cristiano Ronaldo? 👀 | &#39;This is BIG news&#39; | Transfer update 📝',
        'description': 'SUBSCRIBE ▻ http://bit.ly/SSFootballSub PREMIER LEAGUE HIGHLIGHTS ▻ http://bit.ly/SkySportsPLHighlights Sky Sports ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/6M2Zgr6SnHQ/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/6M2Zgr6SnHQ/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/6M2Zgr6SnHQ/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Sky Sports Football',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-07-07T16:10:12Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'U5B3ECfCSo2L95c69clopa96vPE',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'yTnVZk7seE0'
      },
      'snippet': {
        'publishedAt': '2022-07-08T14:20:50Z',
        'channelId': 'UC1YY-cMtrosmFr4KDmlQLcw',
        'title': 'Paulo Dybalaയെ എന്താണ് ഇതുവരെ ആരും വാങ്ങിക്കാത്തത്? പ്രീമിയർ ലീഗ് ലക്ഷ്യം? | Feed Football',
        'description': '',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/yTnVZk7seE0/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/yTnVZk7seE0/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/yTnVZk7seE0/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Feed Football',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-07-08T14:20:50Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'U2puMOSb1jlsWaa4De8w7_zOHdQ',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'YtgzX0D1uX4'
      },
      'snippet': {
        'publishedAt': '2022-02-25T18:00:28Z',
        'channelId': 'UCkCcaU2ScGiGUT5DFQy57sA',
        'title': 'IF FOOTBALLERS WOULD BE GOALKEEPERS!! #Shorts',
        'description': 'IF FOOTBALLERS WOULD BE GOALKEEPERS!! #Shorts Follow me! https://www.instagram.com/akkamist/ FocusDrink: ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/YtgzX0D1uX4/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/YtgzX0D1uX4/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/YtgzX0D1uX4/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Joris',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-02-25T18:00:28Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'uWeVbuEkBe84cKp5Lalxikuo1bY',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'ca0LYQkYv5A'
      },
      'snippet': {
        'publishedAt': '2022-07-08T10:00:24Z',
        'channelId': 'UCUTQeHFbohfQn_9GjYv6HDg',
        'title': 'พีชชี่เข้าใจถ้า &quot;โรนัลโด้&quot; จะทิ้งแมนยู!! | Football Friends EP. 30.2',
        'description': 'หลายหลายแง่มุมของ "พีชชี่" วรันธร กับเรื่องราวของทีมรักอย่างแมนเชสเตอร์ ยูไนเต็ด ที่กำลังเริ่มสร้างทีมใหม่อีกครั้งในยุคของ เอริค เทน ฮาค.',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/ca0LYQkYv5A/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/ca0LYQkYv5A/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/ca0LYQkYv5A/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Football Friends',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-07-08T10:00:24Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'YdFVRtVoAyqw64ONo9FK1yexRTQ',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'nSblgPqKtwo'
      },
      'snippet': {
        'publishedAt': '2021-11-20T12:00:17Z',
        'channelId': 'UC1NaxAHgXHhkjqHn9zXSeMw',
        'title': 'INSANE Long Shot Goals',
        'description': 'Legendary long shot goals scored in football. Paul Pogba amazing long range goal vs Switzerland, Ivan Rakitic vs Tottenham, ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/nSblgPqKtwo/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/nSblgPqKtwo/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/nSblgPqKtwo/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Sir Alex',
        'liveBroadcastContent': 'none',
        'publishTime': '2021-11-20T12:00:17Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'KxUx-C7R06uTiiw_Vbp8frzC_uI',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'U6beee79oII'
      },
      'snippet': {
        'publishedAt': '2022-07-07T11:00:14Z',
        'channelId': 'UCW22zPLx7B0vtS8qNCExekA',
        'title': 'WTF Moments in Football',
        'description': 'WTF Moments in Football #6 ft: Ronaldo, Messi, De Bruyne, Neymar, Grealish... ○ Turn On Notifications To Never Miss an Upload ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/U6beee79oII/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/U6beee79oII/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/U6beee79oII/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'LukaMamson',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-07-07T11:00:14Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'Un13xAb-ZzfEi2qEkqEilAEY58Y',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'WQdNgONXHGw'
      },
      'snippet': {
        'publishedAt': '2022-06-06T13:30:06Z',
        'channelId': 'UC-BlL1ERev9O82Ar4WQmKig',
        'title': 'Football Thug Life Moments',
        'description': 'Hilarious Thug Life moments of some of the worlds best players! All from Cristiano Ronaldo, Messi, Neymar any many more!',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/WQdNgONXHGw/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/WQdNgONXHGw/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/WQdNgONXHGw/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'FOOT4K',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-06-06T13:30:06Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'glk_NfquG4S1LHxFVRoRei3f5Oc',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'ihrq7lDoCnw'
      },
      'snippet': {
        'publishedAt': '2022-07-08T19:32:19Z',
        'channelId': 'UCsAapC5yxX4X0PKZ6HLPJ-A',
        'title': 'BEST FOOTBALL EDITS - FAILS, GOALS &amp; SKILLS (#33)',
        'description': "Subscribe to the channel so you don't miss any videos! Follow: @sanguinayt.",
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/ihrq7lDoCnw/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/ihrq7lDoCnw/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/ihrq7lDoCnw/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Sanguina ',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-07-08T19:32:19Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'soBdPIs5XSIWdTKslZ-C2qTGBfQ',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'MVfqYn9G4Ho'
      },
      'snippet': {
        'publishedAt': '2022-07-08T15:31:43Z',
        'channelId': 'UCyGdKSwfLWGU20Ns1NyoGpQ',
        'title': '1v1 Morpion ! ✅⚽️🎯 | #football #shorts',
        'description': '',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/MVfqYn9G4Ho/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/MVfqYn9G4Ho/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/MVfqYn9G4Ho/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Le Z - Football',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-07-08T15:31:43Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'F7X5vY_NUpa38NCLG-tpJk6Xlyw',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'kPKpY2SJ67A'
      },
      'snippet': {
        'publishedAt': '2022-07-02T15:15:02Z',
        'channelId': 'UCvcLCMmInjvU_p7FEePAo0g',
        'title': 'Moments that Can&#39;t be Repeated in Football',
        'description': "2.000 LIKES ON - Moments that Can't be Repeated in Football ⚽ Please Subscribe To The Channel ⚽ - https://goo-gl.me/NGlF2 ...",
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/kPKpY2SJ67A/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/kPKpY2SJ67A/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/kPKpY2SJ67A/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Dan1s',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-07-02T15:15:02Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'tqPim5w8gkxluZcOiUuL7ZaeoNw',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'xSsiS304iY8'
      },
      'snippet': {
        'publishedAt': '2020-10-18T10:00:12Z',
        'channelId': 'UCSpvzqzfRAJGAWcuYjxWRbw',
        'title': 'Football Matches That Shocked The World',
        'description': 'Football games that shocked the world! Barcelona, Bayern Munich, PSG, Liverpool, Brazil, Germany and more in video!',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/xSsiS304iY8/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/xSsiS304iY8/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/xSsiS304iY8/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'TKHD',
        'liveBroadcastContent': 'none',
        'publishTime': '2020-10-18T10:00:12Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'rPlbwUnXYMejtg97d3-HFONuKZ8',
      'id': {
        'kind': 'youtube#video',
        'videoId': '9GEY7f1lfhs'
      },
      'snippet': {
        'publishedAt': '2022-05-19T12:52:27Z',
        'channelId': 'UCj4OE3L5OVEphzpTRmGTtAQ',
        'title': 'Funny Penalty Moments in Football',
        'description': '20.000 LIKES ON " Epic Penalty "? - Ampyx - Rise ---- https://youtu.be/8h-fqAnIn0A - PIKASONIC - Sky (UXN Release) ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/9GEY7f1lfhs/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/9GEY7f1lfhs/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/9GEY7f1lfhs/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Soccer90v',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-05-19T12:52:27Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'hMTFR9-mh5HkJL14RUk2-lyAccA',
      'id': {
        'kind': 'youtube#video',
        'videoId': '9VGiBEVCcDU'
      },
      'snippet': {
        'publishedAt': '2022-07-08T23:15:10Z',
        'channelId': 'UCz4trs8T2Bk9mSpcAakL3kw',
        'title': 'LSU Football BREAKING NEWS: Jalen Brown Commits! + Does BRIAN KELLY Land a 2023 QB?',
        'description': 'LSU football recruiting landed its first 5-star in Jalen Brown! PHL breaks down the wide receiver from Miami + discusses Brian ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/9VGiBEVCcDU/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/9VGiBEVCcDU/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/9VGiBEVCcDU/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Power Hour LSU with CarterThePower',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-07-08T23:15:10Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'QTKdAK5hIq8x7I5gS-Fk2pv7wcQ',
      'id': {
        'kind': 'youtube#video',
        'videoId': '9YzG5nVc6sg'
      },
      'snippet': {
        'publishedAt': '2021-07-29T07:02:08Z',
        'channelId': 'UCbCmjCuTUZos6Inko4u57UQ',
        'title': 'Soccer Song (Football Song) | CoComelon Nursery Rhymes &amp; Kids Songs',
        'description': 'Come on, lets play, play, play! Join JJ and the CoComelon families in a game of soccer! This fun kids song is all about sports and ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/9YzG5nVc6sg/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/9YzG5nVc6sg/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/9YzG5nVc6sg/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Cocomelon - Nursery Rhymes',
        'liveBroadcastContent': 'none',
        'publishTime': '2021-07-29T07:02:08Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'Zxs47DtSz8QbH3N72HLtJzteIwA',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'B1atp40fLWs'
      },
      'snippet': {
        'publishedAt': '2022-07-07T21:40:01Z',
        'channelId': 'UCAjJYmwcE3o76Sy1nKkr3KA',
        'title': 'Every SEC teams MOST EXPLOSIVE playmaker of 2022 College Football Season.',
        'description': 'Earth shattering. WANNA SUPPORT THE CHANNEL AND GET EXCLUSIVE PATREON BENEFITS https://tinyurl.com/y8lymcmd ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/B1atp40fLWs/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/B1atp40fLWs/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/B1atp40fLWs/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'THE Uncle Lou',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-07-07T21:40:01Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'oq6mhbiNtCepmlQR2pMO6xvFf28',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'NU60bUxpjHM'
      },
      'snippet': {
        'publishedAt': '2022-07-05T13:30:05Z',
        'channelId': 'UC-BlL1ERev9O82Ar4WQmKig',
        'title': 'Football Controversial Moments...',
        'description': "The most rare, strange and controversial moments you've probably seen in Football. Messi, Neymar, Mbappe, Barcelona, Real ...",
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/NU60bUxpjHM/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/NU60bUxpjHM/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/NU60bUxpjHM/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'FOOT4K',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-07-05T13:30:05Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'vcnQhGeTE7hkvVgTAeaGQjFSgn4',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'NygXejdtDh8'
      },
      'snippet': {
        'publishedAt': '2019-04-05T07:00:01Z',
        'channelId': 'UCbCmjCuTUZos6Inko4u57UQ',
        'title': 'The Soccer (Football) Song + More Nursery Rhymes &amp; Kids Songs - CoComelon',
        'description': 'Subscribe for new videos every week! https://www.youtube.com/c/Cocomelon?sub_confirmation=1 A new compilation video, ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/NygXejdtDh8/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/NygXejdtDh8/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/NygXejdtDh8/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Cocomelon - Nursery Rhymes',
        'liveBroadcastContent': 'none',
        'publishTime': '2019-04-05T07:00:01Z'
      }
    },
    {
      'kind': 'youtube#searchResult',
      'etag': 'feUTUjk5wiNyEK_eQLdqVn8cmnw',
      'id': {
        'kind': 'youtube#video',
        'videoId': 'Ri0khe3TH30'
      },
      'snippet': {
        'publishedAt': '2022-06-28T13:30:05Z',
        'channelId': 'UC8MXV8Y2LWMJIjrvRpr_wjg',
        'title': '1 in a Billion Moments in Football',
        'description': 'TURN ON NOTIFICATIONS TO NEVER MISS AN UPLOAD!   Title: 1 in a Billion Moments in Football - Forever – MusicbyAden ...',
        'thumbnails': {
          'default': {
            'url': 'https://i.ytimg.com/vi/Ri0khe3TH30/default.jpg',
            'width': 120,
            'height': 90
          },
          'medium': {
            'url': 'https://i.ytimg.com/vi/Ri0khe3TH30/mqdefault.jpg',
            'width': 320,
            'height': 180
          },
          'high': {
            'url': 'https://i.ytimg.com/vi/Ri0khe3TH30/hqdefault.jpg',
            'width': 480,
            'height': 360
          }
        },
        'channelTitle': 'Sports 360',
        'liveBroadcastContent': 'none',
        'publishTime': '2022-06-28T13:30:05Z'
      }
    }
  ]
}