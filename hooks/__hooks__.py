import thumbnail
import gallery
import album

hooks = {
    'site.start': [thumbnail.create_thumbnails],
    'page.template.pre': [gallery.get_albums, album.get_images]
}

