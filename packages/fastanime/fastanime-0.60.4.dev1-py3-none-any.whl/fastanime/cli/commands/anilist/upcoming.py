import click


@click.command(
    help="Fetch the 15 most anticipited anime", short_help="View upcoming anime"
)
@click.pass_obj
def upcoming(config):
    from ....anilist import AniList
    from ...interfaces.anilist_interfaces import select_anime
    from ...utils.tools import QueryDict

    success, data = AniList.get_upcoming_anime()
    if success:
        anilist_config = QueryDict()
        anilist_config.data = data
        select_anime(config, anilist_config)
