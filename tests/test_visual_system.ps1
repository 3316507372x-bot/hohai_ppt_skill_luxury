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
if ($skill -notmatch 'default visible closing title is `谢谢聆听`') {
    throw 'SKILL.md does not set 谢谢聆听 as the default closing title.'
}
if ($visualSystem -notmatch 'Use `谢谢聆听` as the default visible closing title') {
    throw 'visual-system.md does not set 谢谢聆听 as the default closing title.'
}
if ($skill -notmatch 'Microsoft YaHei.*微软雅黑.*primary Chinese font') {
    throw 'SKILL.md does not set a Windows-compatible Chinese primary font.'
}
if ($visualSystem -notmatch 'Microsoft YaHei.*微软雅黑.*primary face') {
    throw 'visual-system.md does not set a Windows-compatible Chinese primary face.'
}

Write-Output 'visual system check passed'
