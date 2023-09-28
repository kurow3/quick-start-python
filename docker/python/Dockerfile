ARG python_version="3"
FROM python:${python_version}-slim

RUN set -eux \
 && DEBIAN_FRONTEND="noninteractive" \
 && apt-get update \
 && apt-get install -y locales sudo \
 && apt-get install -y git \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

ARG system_lang="C.UTF-8"
RUN set -eux \
 && LANG_REGEX=`echo "${system_lang}" | sed -E -e "s/([\^$.?*+|[\]\{\}()\/\\])/\\\1/g"` \
 && sed -E -i "s/^#+[\t ]*(${LANG_REGEX}.*)$/\1/g" /etc/locale.gen \
 && locale-gen \
 && update-locale LANG="${system_lang}"

ARG system_tz="Etc/UTC"
RUN set -eux \
 && echo "${system_tz}" > /etc/timezone

ARG user_name="vscode"
ARG user_uid="1000"
ARG user_gid="${user_uid}"
ARG user_shell="/usr/bin/bash"
RUN set -eux \
 && groupadd --gid "${user_gid}" "${user_name}" \
 && useradd --uid "${user_uid}" --gid "${user_gid}" --shell "${user_shell}" -m "${user_name}" \
 && echo "${user_name} ALL=(root) NOPASSWD:ALL" > "/etc/sudoers.d/${user_name}" \
 && chmod 0440 "/etc/sudoers.d/${user_name}"

ARG workspace_dir="/workspace"
RUN set -eux \
 && mkdir -p "${workspace_dir}" \
 && chown "${user_uid}":"${user_gid}" "${workspace_dir}"

USER "${user_name}"
ENV LANG="${system_lang}" \
    TZ="${system_tz}"
WORKDIR "${workspace_dir}"

COPY ./requirements.txt ./requirements-dev.txt ./
RUN set -eux \
 && pip install --no-cache-dir -r ./requirements.txt \
 && pip install --no-cache-dir -r ./requirements-dev.txt

CMD ["bash"]
