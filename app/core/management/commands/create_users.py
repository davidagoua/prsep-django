from django.core.management.base import BaseCommand
from mon_app.models import Departement, Role  # Adapte "mon_app" !
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = "Crée pour chaque département un utilisateur pour chaque rôle"

    def handle(self, *args, **kwargs):
        departements = Departement.objects.all()
        roles = Role.objects.all()
        created = 0

        for departement in departements:
            for role in roles:
                # On crée un username unique pour chaque combinaison
                username = f"{departement.name.lower()}_{role.name.lower()}"
                # Vérifie si l'utilisateur existe déjà
                if not User.objects.filter(username=username).exists():
                    user = User.objects.create_user(
                        username=username,
                        password="pass1234",  # Pense à forcer le changement de mot de passe !
                    )
                    # Ajoute les relations si besoin
                    if hasattr(user, "departement"):
                        user.departement = departement
                    if hasattr(user, "role"):
                        user.role = role
                    user.save()
                    self.stdout.write(self.style.SUCCESS(
                        f"Utilisateur '{username}' créé pour {departement.name} avec le rôle {role.name}"
                    ))
                    created += 1
                else:
                    self.stdout.write(self.style.WARNING(
                        f"L'utilisateur '{username}' existe déjà"
                    ))

        self.stdout.write(self.style.SUCCESS(f"{created} utilisateurs ont été créés"))