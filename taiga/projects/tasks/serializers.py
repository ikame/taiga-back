# Copyright (C) 2014 Andrey Antukh <niwi@niwi.be>
# Copyright (C) 2014 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014 David Barragán <bameda@dbarragan.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from rest_framework import serializers

from taiga.base.serializers import PickleField

from . import models


class TaskSerializer(serializers.ModelSerializer):
    tags = PickleField(required=False, default=[])
    comment = serializers.SerializerMethodField("get_comment")
    milestone_slug = serializers.SerializerMethodField("get_milestone_slug")
    blocked_note_html = serializers.SerializerMethodField("get_blocked_note_html")
    description_html = serializers.SerializerMethodField("get_description_html")

    class Meta:
        model = models.Task

    def get_comment(self, obj):
        return ""

    def get_milestone_slug(self, obj):
        if obj.milestone:
            return obj.milestone.slug
        else:
            return None

    def get_blocked_note_html(self, obj):
        return mdrender(obj.project, obj.blocked_note)

    def get_description_html(self, obj):
        return mdrender(obj.project, obj.description)
