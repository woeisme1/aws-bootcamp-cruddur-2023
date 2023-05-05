from datetime import datetime, timedelta, timezone
class NotificationsActivities:
  def run():
    now = datetime.now(timezone.utc).astimezone()
    results = [{
      'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
      'handle':  'Snoop dogg',
      'message': 'Cloud is fun!',
      'created_at': (now - timedelta(days=2)).isoformat(),
      'expires_at': (now + timedelta(days=5)).isoformat(),
      'likes_count': 552,
      'replies_count': 54,
      'reposts_count': 99,
      'replies': [{
        'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
        'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
        'handle':  'UncleShimura',
        'message': 'You have no honor!',
        'likes_count': 100,
        'replies_count': 9,
        'reposts_count': 3,
        'created_at': (now - timedelta(days=2)).isoformat()
      }],
    },
    ]
    return results