from flask import Flask, flash, redirect, render_template, render_template_string, request, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from crypt import methods