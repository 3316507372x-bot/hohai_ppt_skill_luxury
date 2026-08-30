$root = Split-Path -Parent $PSScriptRoot
$skill = Get-Content -LiteralPath (Join-Path $root 'SKILL.md') -Raw -Encoding UTF8
$visualSystem = Get-Content -LiteralPath (Join-Path $root 'references\visual-system.md') -Raw -Encoding UTF8
$provenance = Get-Content -LiteralPath (Join-Path $root 'assets\provenance.json') -Raw -Encoding UTF8

if ($skill -notmatch '83% on content pages') {
    throw 'SKILL.md does not set the content white wash to 83 percent.'
}
if ($visualSystem -notmatch 'Content pages:.*83%') {
    throw 'visual-system.md does not set the content white wash to 83 percent.'
}
if ($visualSystem -notmatch 'white overlay at about \*\*83% opacity\*\*') {
    throw 'visual-system.md standard-content guidance is not set to 83 percent.'
}
if ($provenance -notmatch 'divider,.*83% content') {
    throw 'provenance.json does not record the 83 percent content wash.'
}

Write-Output 'visual system check passed'
