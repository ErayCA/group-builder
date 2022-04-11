from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


# Databse model definitions
class Cohort(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cohortname = db.Column(db.String(300), unique=False, nullable=True)

    def __repr__(self):
        return '<Cohort %r>' % self.id

    def __init__(self, id, cohortname):
        self.id = id
        self.cohortname = cohortname

    def jsonify(self):
        data = {
            'id': self.id,
            'cohortname': self.cohortname
        }
        return (data)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(300), unique=False, nullable=True)
    surname = db.Column(db.String(300), unique=False, nullable=True)
    email = db.Column(db.String(600), unique=True, nullable=False)
    password = db.Column(db.String(600), unique=False, nullable=False)
    registered = db.Column(db.Boolean, unique=False, nullable=False)
    cohortID = db.Column(db.Integer, db.ForeignKey(
        'cohort.id'), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def __init__(self, id, firstname, surname, email, password, registered, cohortID):
        self.id = id
        self.firstname = firstname
        self.surname = surname
        self.email = email
        self.password = password
        self.registered = registered
        self.cohortID = cohortID

    def jsonify(self):
        data = {
            'id': self.id,
            'firstname': self.firstname,
            'surname': self.surname,
            'email': self.email,
            'registered': self.registered,
            'cohortID': self.cohortID
        }
        return (data)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    projectname = db.Column(db.String(300), unique=False, nullable=True)
    managerID = db.Column(db.Integer, unique=False, nullable=False)
    cohortID = db.Column(db.Integer, db.ForeignKey(
        'cohort.id'), unique=False, nullable=False)

    def __repr__(self):
        return '<Project %r>' % self.id

    def __init__(self, id, projectname, managerID, cohortID):
        self.id = id
        self.projectname = projectname
        self.managerID = managerID
        self.cohortID = cohortID

    def jsonify(self):
        data = {
            'id': self.id,
            'projectname': self.projectname,
            'managerID': self.managerID,
            'cohortID': self.cohortID
        }
        return (data)


class Confirmation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    confirmationname = db.Column(db.String(300), unique=False, nullable=True)

    def __repr__(self):
        return '<Confirmation %r>' % self.id

    def __init__(self, id, confirmationname):
        self.id = id
        self.confirmationname = confirmationname

    def jsonify(self):
        data = {
            'id': self.id,
            'confirmationname': self.confirmationname
        }
        return (data)


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    linkerID = db.Column(db.Integer, db.ForeignKey(
        'user.id'), unique=False, nullable=False)
    linkeeID = db.Column(db.Integer, db.ForeignKey(
        'user.id'), unique=False, nullable=False)
    linkprojectID = db.Column(db.Integer, db.ForeignKey(
        'project.id'), unique=False, nullable=False)
    linkconfirmationID = db.Column(db.Integer, db.ForeignKey(
        'confirmation.id'), unique=False, nullable=False)

    def __repr__(self):
        return '<Link %r>' % self.id

    def __init__(self, id, linkerID, linkeeID, linkprojectID, linkconfirmationID):
        self.id = id
        self.linkerID = linkerID
        self.linkeeID = linkeeID
        self.linkprojectID = linkprojectID
        self.linkconfirmationID = linkconfirmationID

    def jsonify(self):
        data = {
            'id': self.id,
            'linkerID': self.linkerID,
            'linkeeID': self.linkeeID,
            'linkprojectID': self.linkprojectID,
            'linkconfirmationID': self.linkconfirmationID
        }
        return (data)


class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modulename = db.Column(db.String(300), unique=False, nullable=True)
    moduleleaderID = db.Column(db.Integer, db.ForeignKey(
        'user.id'), unique=False, nullable=False)
    modulecohortID = db.Column(db.Integer, db.ForeignKey(
        'cohort.id'), unique=False, nullable=False)

    def __repr__(self):
        return '<Module %r>' % self.id

    def __init__(self, id, modulename, moduleleaderID, modulecohortID):
        self.id = id
        self.modulename = modulename
        self.moduleleaderID = moduleleaderID
        self.modulecohortID = modulecohortID

    def jsonify(self):
        data = {
            'id': self.id,
            'modulename': self.modulename,
            'moduleleaderID': self.moduleleaderID,
            'modulecohortID': self.modulecohortID
        }
        return (data)


class ModuleMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modulememberuserID = db.Column(db.Integer, db.ForeignKey(
        'user.id'), unique=False, nullable=False)
    modulemembermoduleID = db.Column(db.Integer, db.ForeignKey(
        'module.id'), unique=False, nullable=False)
    modulememberorder = db.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self):
        return '<ModuleMember %r>' % self.id

    def __init__(self, id, modulememberuserID, modulemembermoduleID, modulememberorder):
        self.id = id
        self.modulememberuserID = modulememberuserID
        self.modulemembermoduleID = modulemembermoduleID
        self.modulememberorder = modulememberorder

    def jsonify(self):
        data = {
            'id': self.id,
            'modulememberuserID': self.modulememberuserID,
            'modulemembermoduleID': self.modulemembermoduleID,
            'modulememberorder': self.modulememberorder
        }
        return (data)


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    groupname = db.Column(db.String(300), unique=False, nullable=True)
    groupprojectID = db.Column(db.Integer, db.ForeignKey(
        'project.id'), unique=False, nullable=False)

    def __repr__(self):
        return '<Group %r>' % self.id

    def __init__(self, id, groupname, groupprojectID):
        self.id = id
        self.groupname = groupname
        self.groupprojectID = groupprojectID

    def jsonify(self):
        data = {
            'id': self.id,
            'groupname': self.groupname,
            'groupprojectID': self.groupprojectID
        }
        return (data)


class GroupMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    groupmemberuserID = db.Column(db.Integer, db.ForeignKey(
        'user.id'), unique=False, nullable=False)
    groupmembergroupID = db.Column(db.Integer, db.ForeignKey(
        'group.id'), unique=False, nullable=False)

    def __repr__(self):
        return '<GroupMember %r>' % self.id

    def __init__(self, id, groupmemberuserID, groupmembergroupID):
        self.id = id
        self.groupmemberuserID = groupmemberuserID
        self.groupmembergroupID = groupmembergroupID

    def jsonify(self):
        data = {
            'id': self.id,
            'groupmemberuserID': self.groupmemberuserID,
            'groupmembergroupID': self.groupmembergroupID
        }
        return (data)


class Affinity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    affinityname = db.Column(db.String(300), unique=False, nullable=True)

    def __repr__(self):
        return '<Affinity %r>' % self.id

    def __init__(self, id, affinityname):
        self.id = id
        self.affinityname = affinityname

    def jsonify(self):
        data = {
            'id': self.id,
            'affinityname': self.affinityname
        }
        return (data)


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    likeaffinityID = db.Column(db.Integer, db.ForeignKey(
        'affinity.id'), unique=False, nullable=False)
    likerID = db.Column(db.Integer, db.ForeignKey(
        'user.id'), unique=False, nullable=False)
    likeeID = db.Column(db.Integer, db.ForeignKey(
        'user.id'), unique=False, nullable=False)

    def __repr__(self):
        return '<Like %r>' % self.id

    def __init__(self, id, likeaffinityID, likerID, likeeID):
        self.id = id
        self.likeaffinityID = likeaffinityID
        self.likerID = likerID
        self.likee = likeeID

    def jsonify(self):
        data = {
            'id': self.id,
            'likeaffinityID': self.likeaffinityID,
            'likerID': self.likerID,
            'likeeID': self.likeeID,
        }
        return (data)