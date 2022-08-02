comments = [
    {
        'id': 1,
        'content': 'Comment',
        'blog_id': 1
    },
    {
        'id': 2,
        'content': 'Comment 2',
        'blog_id': 1
    },
    {
        'id': 3,
        'content': 'Comment 3',
        'blog_id': 2
    }
]


def create_comment(content,blog_id):
    comment_data = {
        'id': len(comments) + 1 ,
        'content': content,
        'blog_id': blog_id
    }
    comments.append(comment_data)
    return comment_data


def get_comments(blog_id):
    cs = []
    for comment in comments:
        if comment['blog_id'] == blog_id:
            cs.append(comment)
    return cs
    # return list(filter(lambda comment: comment['blog_id'] ==blog_id, commnets))