from .extensions import scheduler, db

def init_scheduler(app):
    def add_resources():
        with app.app_context():
            from .models import Village
            villages = Village.query.all()
            for village in villages:
                village.wood += 10
                village.stones += 5
            db.session.commit()

    scheduler.init_app(app)
    scheduler.add_job(id='add_resources', func=add_resources, trigger='interval', seconds=5)
    scheduler.start()