# opt-nesi-bin

Scripts from `/opt/nesi/bin`.

This repository manages user facing commands on Mahuika (for internal tools see `/opt/nesi/sbin`).

Please try to record your changes 🙂

- Keep scripts simple and readable.
- Test before merging.
- All changes tracked through Git!.

## For NeSI Staff

### Creating your user copy

On Mahuika:

```sh
cd /nesi/project/nesi99999/$USER
git clone https://github.com/nesi/opt-nesi-bin.git
cd opt-nesi-bin
```

### Making Changes

Make sure your local copy is up to date, then create a feature branch:

```sh
git pull origin main
git checkout -b <short-description-of-change>
```

Make your changes and commit with a clear message describing what changed and why:

```sh
git commit -m "Fix incorrect path handling in nn_count_files"
```

### Testing

Before creating a PR:

- Test the command locally.
- Ensure you are running the local version (e.g. `./nn_my_tool`).
- Check command works outside its directory (e.g. `opt-nesi-bin/nn_my_tool`).
- Confirm help output works.

Then push:

```sh
git push origin <branch_name>
```

### Pull Request

Create a pull request in GitHub to merge your feature branch into `main`.

Keep PR descriptions short but clear.

Requires 1 reveiw to merge.

### Deployment

Once your change is merged:

```sh
sudo -i -u nesi-apps-admin
cd /opt/nesi/bin
git pull origin main
```

Permissions should be automatically changed in post checkout hooks.

DONT modify files directly in `/opt/nesi/bin` changes must come through Git!

## Script Guidelines

### Naming

- Commands must start with `nn`
- Use `snake_case`
- Keep names short and descriptive

e.g:

```sh
nn_project_summary
```

### File + Symlink Pattern

Scripts should have the correct suffix (e.g. `.sh`)  
Create a symlink without the suffix

```sh
ln -s nn_my_tool.sh nn_my_tool
```

### Shebang

Always include an explicit interpreter

```sh
#!/bin/bash
```

Consider including:

```sh
set -euo pipefail
```

Preferably Python scripts should use the system Python.

```sh
#!/bin/python
```

### Help Output

Commands should print helpful output when called with incorrect arguments or flags.

- Short description
- Usage syntax
- Required arguments
- Optional flags
- Examples (if helpful)

## Deprecating a Command

If replacing a command:

- Leave the old command in place.
- Print a warning directing users to the new command.
- Remove after x amount of time passed.

## What commands do

TODO: Move main description into command itself.

### `aws`

Symlink to `/opt/nesi/share/aws-cli/v2/current/bin/aws`

### `aws_completer`

symlink to `/opt/nesi/share/aws-cli/v2/current/bin/aws_completer`

### `cloudflared`

*Binary not in repo*

Cloudflare tunnel connector. Used by Lai Kei.

### db_tunnel_ctl

Symlink to `db_tunnel_ctl`

### diskquotas    

### `get_system_tag.sh`

Dunno. Seems broken.

### `gprof2dot`

*Binary not in repo*

### grpfix

### home_directory_whitelist.txt

Used by audit maybe?

### `jupyterbash`

Used by jupyter for something.
Owned by root.

### `logger.py`

Seems to forward stdin to syslogs?

### `nn_archive_files`

A wrapper to bundle a list of files up into a SquashFS archive, creating
a list of checksums in the process (to help the user to identify bitrot later).
probably deprecated.

### `nn_audit_home_directories`

Shows all home directories with 'incorrect' permissions.
Questionable use to users.

### `nn_check_quota`

Symlink to `nn_storage_quota`

### `nn_countfiles`

Helper script to count files under a directory (find/wc/tr, etc). 
Should just run.

### `nn_dir_contents`

Just a report on a directory. `bash/find/awk/du`

### `nn_doomed_list`

Helper script that seems to report on files that are about to be deletd.
It must work in conjunction with some other process that produces the doomed file:
`/nesi/nobackup/<project>/.policy/to_delete/latest.filelist.gz`
because it reads those and prints them out.

### `nn_group_members`

Print out active members of a group. Should just run as is.

### `nn_job_priorities`

`sprio | head -n 1 && (sprio | tail -n +2 | sort -n -r -k3,3)`

### `nn_my_queued_jobs`

basically, the output of
`squeue -u $(whoami) -t PENDING -o "%14a %.13i %20j %19V %6q %.4D %.4C %.10m %.8Q %19S %r"`
(sorted in a particular order)

### `nn_seff`

`sacct -P -n -a --format JobID,User,State,Cluster,AllocCPUS,REQMEM,TotalCPU,Elapsed,MaxRSS,NNodes,NTasks -j <job_id>`
this is a python3 script. 

### nn_sshare_sorted

### `nn_storage_quota`

Modified for weka to use the df command. Drops inode reporting.

### nn_weekly_job_efficiency_report.sh

### profile_data

### `profile_plot`

Plot data from a Slurm HDF5 profile file generated with sh5util.

Writes a 4-panel plot into a PNG file.
 - CPU utilisation
 - Memory Utilisation (RSS)
 - I/O Rate
 - Cumulative I/O

### `tunnel_ctl`

Helper script for managing cloudflare tunnels

### `sudosh-allow`

opt in, and allow yourself to be impersonated (places the calling user into the impersonated group)

### `sudosh-disallow`

opt out (removes the calling user from the impersonated group)

### `sudosh-grp`

helper function called by the above two utilities to add/remove user from the impersonated group (this requires a sudo rule, since it needs freeipa privileges for maintaining groups)

### `sudosh-ls`

list sessions in which the calling user has been impersonated, along with metadata about each session (who did it, when, how long did it last)

and the out of the box sudosh utilities

### `sudosh`

*Binary not in repo.*

Impersonators call this, using `sudo -u <user> sudosh`

### `sudosh-replay`

*Binary not in repo.*

Users can call this to replay sessions in which they were impersonated. root can view all sessions
