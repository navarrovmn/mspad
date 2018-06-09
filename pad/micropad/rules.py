import rules


@rules.predicate
def is_page_owner(user, archive):
    print(user.username)
    print(archive.owner_username)
    if archive.owner_username:
        return user.username == archive.owner_username
    else:
        archive.owner_username = user.username
        archive.save()
        return True
        

@rules.predicate
def page_is_locked(page):
    return page.lock


#@TODO create rule logic
@rules.predicate
def is_editor(user, archive):
    return is_page_owner(user, archive)

@rules.predicate
def can_edit_page(user, page):
    if page_is_locked(page):
        if is_editor(user, page) or is_page_owner(user, page):
            return True
        else:
            return False
    else:
        return True

rules.add_rule('can_edit_page', can_edit_page)
rules.add_rule('is_page_owner', is_page_owner)