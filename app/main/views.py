import os

from flask import render_template,request, redirect, url_for, abort,flash
from . import main
from .forms import PostForm
from ..models import Post,Comment
from .. import db
from app.requests import getQuotes
from flask_login import login_required,current_user

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    quotes=getQuotes()
    posts = Post.query.all()
    title='Quotes Blog'
    return render_template('index.html',title=title,quotes=quotes,posts=posts, current_user=current_user)



@main.route("/new_post", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data,author=current_user)
        post.save()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.index'))
    return render_template('new_post.html', title='New Post',
                           form=form, legend='New Post')

@main.route("/post/<int:post_id>")
@login_required
def mypost(post_id):
    comments = Comment.query.filter_by(post_id=post_id).all()
    print(comments)
    heading = 'comments'
    post = Post.query.get_or_404(post_id)
    return render_template('posts.html', title=post.title, post=post, comments=comments, heading=heading)

@main.route('/comment/<post_id>', methods=['Post', 'GET'])

def comment(post_id):
    comment = request.form.get('newcomment')
    new_comment = Comment(comment=comment, user_id=current_user._get_current_object().id, post_id=post_id)
    new_comment.save()
    return redirect(url_for('main.mypost', post_id=post_id))
