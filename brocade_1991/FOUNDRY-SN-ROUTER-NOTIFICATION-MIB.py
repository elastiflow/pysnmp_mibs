# SNMP MIB module (FOUNDRY-SN-ROUTER-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/brocade_1991/FOUNDRY-SN-ROUTER-NOTIFICATION-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:18:38 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(snAgGblTrapMessage,
 snAgentBrdIndex,
 snAgentBrdModuleStatus,
 snChasFanDescription,
 snChasFanIndex,
 snChasPwrSupplyDescription,
 snChasPwrSupplyIndex,
 snChasUnitIndex) = mibBuilder.importSymbols(
    "FOUNDRY-SN-AGENT-MIB",
    "snAgGblTrapMessage",
    "snAgentBrdIndex",
    "snAgentBrdModuleStatus",
    "snChasFanDescription",
    "snChasFanIndex",
    "snChasPwrSupplyDescription",
    "snChasPwrSupplyIndex",
    "snChasUnitIndex")

(foundry,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "foundry")

(snVLanByPortCfgVLanId,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "snVLanByPortCfgVLanId")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

snTraps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 0)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

snTrapModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 28)
)
snTrapModuleInserted.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex")
)
if mibBuilder.loadTexts:
    snTrapModuleInserted.setStatus(
        "current"
    )

snTrapModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 29)
)
snTrapModuleRemoved.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex")
)
if mibBuilder.loadTexts:
    snTrapModuleRemoved.setStatus(
        "current"
    )

snTrapChasPwrSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 30)
)
snTrapChasPwrSupplyFailed.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasPwrSupplyIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snChasPwrSupplyDescription"))
)
if mibBuilder.loadTexts:
    snTrapChasPwrSupplyFailed.setStatus(
        "current"
    )

snTrapChasFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 31)
)
snTrapChasFanFailed.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasFanIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snChasFanDescription"))
)
if mibBuilder.loadTexts:
    snTrapChasFanFailed.setStatus(
        "current"
    )

snTrapVrrpIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 34)
)
snTrapVrrpIfStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapVrrpIfStateChange.setStatus(
        "current"
    )

snTrapMgmtModuleRedunStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 35)
)
snTrapMgmtModuleRedunStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMgmtModuleRedunStateChange.setStatus(
        "current"
    )

snTrapTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 36)
)
snTrapTemperatureWarning.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTemperatureWarning.setStatus(
        "current"
    )

snTrapAccessListDeny = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 37)
)
snTrapAccessListDeny.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapAccessListDeny.setStatus(
        "current"
    )

snTrapMacFilterDeny = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 38)
)
snTrapMacFilterDeny.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacFilterDeny.setStatus(
        "current"
    )

snTrapIcmpLocalExceedBurst = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 51)
)
snTrapIcmpLocalExceedBurst.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapIcmpLocalExceedBurst.setStatus(
        "current"
    )

snTrapIcmpTransitExceedBurst = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 52)
)
snTrapIcmpTransitExceedBurst.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapIcmpTransitExceedBurst.setStatus(
        "current"
    )

snTrapTcpLocalExceedBurst = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 53)
)
snTrapTcpLocalExceedBurst.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTcpLocalExceedBurst.setStatus(
        "current"
    )

snTrapTcpTransitExceedBurst = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 54)
)
snTrapTcpTransitExceedBurst.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTcpTransitExceedBurst.setStatus(
        "current"
    )

snTrapDuplicateIp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 56)
)
snTrapDuplicateIp.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapDuplicateIp.setStatus(
        "current"
    )

snTrapMplsProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 57)
)
snTrapMplsProblem.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMplsProblem.setStatus(
        "current"
    )

snTrapMplsException = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 58)
)
snTrapMplsException.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMplsException.setStatus(
        "current"
    )

snTrapMplsAudit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 59)
)
snTrapMplsAudit.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMplsAudit.setStatus(
        "current"
    )

snTrapMplsDeveloper = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 60)
)
snTrapMplsDeveloper.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMplsDeveloper.setStatus(
        "current"
    )

snTrapNoBmFreeQueue = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 61)
)
snTrapNoBmFreeQueue.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapNoBmFreeQueue.setStatus(
        "current"
    )

snTrapSmcDmaDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 62)
)
snTrapSmcDmaDrop.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSmcDmaDrop.setStatus(
        "current"
    )

snTrapSmcBpDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 63)
)
snTrapSmcBpDrop.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSmcBpDrop.setStatus(
        "current"
    )

snTrapBmWriteSeqDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 64)
)
snTrapBmWriteSeqDrop.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapBmWriteSeqDrop.setStatus(
        "current"
    )

snTrapRunningConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 73)
)
snTrapRunningConfigChanged.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapRunningConfigChanged.setStatus(
        "current"
    )

snTrapStartupConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 74)
)
snTrapStartupConfigChanged.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapStartupConfigChanged.setStatus(
        "current"
    )

snTrapUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 75)
)
snTrapUserLogin.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapUserLogin.setStatus(
        "current"
    )

snTrapUserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 76)
)
snTrapUserLogout.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapUserLogout.setStatus(
        "current"
    )

snTrapPortSecurityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 77)
)
snTrapPortSecurityViolation.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPortSecurityViolation.setStatus(
        "current"
    )

snTrapPortSecurityShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 78)
)
snTrapPortSecurityShutdown.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPortSecurityShutdown.setStatus(
        "current"
    )

snTrapMrpStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 79)
)
snTrapMrpStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMrpStateChange.setStatus(
        "current"
    )

snTrapMrpCamError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 80)
)
snTrapMrpCamError.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMrpCamError.setStatus(
        "current"
    )

snTrapChasPwrSupplyOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 81)
)
snTrapChasPwrSupplyOK.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasPwrSupplyIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snChasPwrSupplyDescription"))
)
if mibBuilder.loadTexts:
    snTrapChasPwrSupplyOK.setStatus(
        "current"
    )

snTrapVrrpeIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 82)
)
snTrapVrrpeIfStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapVrrpeIfStateChange.setStatus(
        "current"
    )

snTrapVsrpIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 83)
)
snTrapVsrpIfStateChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapVsrpIfStateChange.setStatus(
        "current"
    )

snTrapSrcIpAddressViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 84)
)
snTrapSrcIpAddressViolation.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSrcIpAddressViolation.setStatus(
        "current"
    )

snTrapClientLoginReject = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 110)
)
snTrapClientLoginReject.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapClientLoginReject.setStatus(
        "current"
    )

snTrapLocalUserConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 111)
)
snTrapLocalUserConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapLocalUserConfigChange.setStatus(
        "current"
    )

snTrapVlanConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 112)
)
snTrapVlanConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapVlanConfigChange.setStatus(
        "current"
    )

snTrapAclConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 113)
)
snTrapAclConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapAclConfigChange.setStatus(
        "current"
    )

snTrapMacFilterConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 114)
)
snTrapMacFilterConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacFilterConfigChange.setStatus(
        "current"
    )

snTrapSNMPConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 115)
)
snTrapSNMPConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSNMPConfigChange.setStatus(
        "current"
    )

snTrapSyslogConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 116)
)
snTrapSyslogConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSyslogConfigChange.setStatus(
        "current"
    )

snTrapPasswordConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 117)
)
snTrapPasswordConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPasswordConfigChange.setStatus(
        "current"
    )

snTrapServerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 118)
)
snTrapServerStatusChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapServerStatusChange.setStatus(
        "current"
    )

snTrapDot1xSecurityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 131)
)
snTrapDot1xSecurityViolation.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapDot1xSecurityViolation.setStatus(
        "current"
    )

snTrapDot1xPortLinkChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 132)
)
snTrapDot1xPortLinkChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapDot1xPortLinkChange.setStatus(
        "current"
    )

snTrapDot1xPortControlChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 133)
)
snTrapDot1xPortControlChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapDot1xPortControlChange.setStatus(
        "current"
    )

snTrapDot1xVlanIdChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 134)
)
snTrapDot1xVlanIdChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapDot1xVlanIdChange.setStatus(
        "current"
    )

snTrapDot1xFilterSetupFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 135)
)
snTrapDot1xFilterSetupFailure.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapDot1xFilterSetupFailure.setStatus(
        "current"
    )

snTrapDot1xError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 136)
)
snTrapDot1xError.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapDot1xError.setStatus(
        "current"
    )

snTrapPortConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 137)
)
snTrapPortConfigChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPortConfigChange.setStatus(
        "current"
    )

snTrapMacAuthVlanIdChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 138)
)
snTrapMacAuthVlanIdChange.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapMacAuthVlanIdChange.setStatus(
        "current"
    )

snTrapUDLDLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 145)
)
snTrapUDLDLinkDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapUDLDLinkDown.setStatus(
        ""
    )

snTrapUDLDLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 146)
)
snTrapUDLDLinkUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapUDLDLinkUp.setStatus(
        ""
    )

snTrapStpRootGuardDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 150)
)
snTrapStpRootGuardDetect.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByPortCfgVLanId"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapStpRootGuardDetect.setStatus(
        "current"
    )

snTrapStpRootGuardExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 151)
)
snTrapStpRootGuardExpire.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByPortCfgVLanId"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapStpRootGuardExpire.setStatus(
        "current"
    )

snTrapStpBPDUGuardDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 152)
)
snTrapStpBPDUGuardDetect.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByPortCfgVLanId"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapStpBPDUGuardDetect.setStatus(
        "current"
    )

snTrapLACPLinkStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 155)
)
snTrapLACPLinkStateChange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapLACPLinkStateChange.setStatus(
        "current"
    )

snTrapOpticalMonitoringNotFoundryOptics = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 156)
)
snTrapOpticalMonitoringNotFoundryOptics.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapOpticalMonitoringNotFoundryOptics.setStatus(
        "current"
    )

snTrapOpticalMonitoringFoundryOpticsNotCapable = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 157)
)
snTrapOpticalMonitoringFoundryOpticsNotCapable.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapOpticalMonitoringFoundryOpticsNotCapable.setStatus(
        "current"
    )

snTrapSTPBPDUGuardExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 160)
)
snTrapSTPBPDUGuardExpire.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByPortCfgVLanId"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapSTPBPDUGuardExpire.setStatus(
        "current"
    )

snTrapIfIndexAssignmentChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 172)
)
snTrapIfIndexAssignmentChanged.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapIfIndexAssignmentChanged.setStatus(
        "current"
    )

snTrapPBRConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 173)
)
snTrapPBRConfigChanged.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPBRConfigChanged.setStatus(
        "current"
    )

snTrapModuleStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 176)
)
snTrapModuleStatusChange.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasUnitIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgentBrdModuleStatus"),
        ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage"))
)
if mibBuilder.loadTexts:
    snTrapModuleStatusChange.setStatus(
        "current"
    )

snTrapChasHighSpeedFansNeeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 177)
)
snTrapChasHighSpeedFansNeeded.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapChasHighSpeedFansNeeded.setStatus(
        "current"
    )

snTrapSysmaxReverted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 178)
)
snTrapSysmaxReverted.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSysmaxReverted.setStatus(
        "current"
    )

snTrapSysmaxLeftLowMem = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 179)
)
snTrapSysmaxLeftLowMem.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSysmaxLeftLowMem.setStatus(
        "current"
    )

snTrapSysMemoryLowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 180)
)
snTrapSysMemoryLowThreshold.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSysMemoryLowThreshold.setStatus(
        "current"
    )

snTrapSysMemoryOutThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 181)
)
snTrapSysMemoryOutThreshold.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSysMemoryOutThreshold.setStatus(
        "current"
    )

snTrapChasFanOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1000)
)
snTrapChasFanOK.setObjects(
      *(("FOUNDRY-SN-AGENT-MIB", "snChasFanIndex"),
        ("FOUNDRY-SN-AGENT-MIB", "snChasFanDescription"))
)
if mibBuilder.loadTexts:
    snTrapChasFanOK.setStatus(
        "current"
    )

snTrapTemperatureOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1001)
)
snTrapTemperatureOK.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTemperatureOK.setStatus(
        "current"
    )

snTrapCAMOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1002)
)
snTrapCAMOverflow.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapCAMOverflow.setStatus(
        "current"
    )

snTrapOpticalMonitoringWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1003)
)
snTrapOpticalMonitoringWarning.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapOpticalMonitoringWarning.setStatus(
        "current"
    )

snTrapOpticalMonitoringAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1004)
)
snTrapOpticalMonitoringAlarm.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapOpticalMonitoringAlarm.setStatus(
        "current"
    )

snTrapOpticalMonitoringError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1005)
)
snTrapOpticalMonitoringError.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapOpticalMonitoringError.setStatus(
        "current"
    )

snTrapPosMonitoringWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1006)
)
snTrapPosMonitoringWarning.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPosMonitoringWarning.setStatus(
        "current"
    )

snTrapPosMonitoringAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1007)
)
snTrapPosMonitoringAlarm.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPosMonitoringAlarm.setStatus(
        "current"
    )

snTrapPosMonitoringError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1008)
)
snTrapPosMonitoringError.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapPosMonitoringError.setStatus(
        "current"
    )

snTrapXfpSfpIncompatibleOptics = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1009)
)
snTrapXfpSfpIncompatibleOptics.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapXfpSfpIncompatibleOptics.setStatus(
        "current"
    )

snTrapTMLoggingStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1015)
)
snTrapTMLoggingStart.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTMLoggingStart.setStatus(
        "current"
    )

snTrapTMLoggingStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1016)
)
snTrapTMLoggingStop.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTMLoggingStop.setStatus(
        "current"
    )

snTrapTMLoggingRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1017)
)
snTrapTMLoggingRestart.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTMLoggingRestart.setStatus(
        "current"
    )

snTrapXfpSfpNotFoundryOptics = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1018)
)
snTrapXfpSfpNotFoundryOptics.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapXfpSfpNotFoundryOptics.setStatus(
        "current"
    )

snTrapTMRecoverySlotReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1019)
)
snTrapTMRecoverySlotReset.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapTMRecoverySlotReset.setStatus(
        "current"
    )

snTrapSFMLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1100)
)
snTrapSFMLinkDown.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSFMLinkDown.setStatus(
        "current"
    )

snTrapSFMLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1101)
)
snTrapSFMLinkUp.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapSFMLinkUp.setStatus(
        "current"
    )

snTrapChassisFanSpeedLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1200)
)
snTrapChassisFanSpeedLow.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapChassisFanSpeedLow.setStatus(
        "current"
    )

snTrapChassisFanSpeedMedium = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1201)
)
snTrapChassisFanSpeedMedium.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapChassisFanSpeedMedium.setStatus(
        "current"
    )

snTrapChassisFanSpeedMedHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1202)
)
snTrapChassisFanSpeedMedHigh.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapChassisFanSpeedMedHigh.setStatus(
        "current"
    )

snTrapChassisFanSpeedHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1203)
)
snTrapChassisFanSpeedHigh.setObjects(
    ("FOUNDRY-SN-AGENT-MIB", "snAgGblTrapMessage")
)
if mibBuilder.loadTexts:
    snTrapChassisFanSpeedHigh.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-SN-ROUTER-NOTIFICATION-MIB",
    **{"snTraps": snTraps,
       "snTrapModuleInserted": snTrapModuleInserted,
       "snTrapModuleRemoved": snTrapModuleRemoved,
       "snTrapChasPwrSupplyFailed": snTrapChasPwrSupplyFailed,
       "snTrapChasFanFailed": snTrapChasFanFailed,
       "snTrapVrrpIfStateChange": snTrapVrrpIfStateChange,
       "snTrapMgmtModuleRedunStateChange": snTrapMgmtModuleRedunStateChange,
       "snTrapTemperatureWarning": snTrapTemperatureWarning,
       "snTrapAccessListDeny": snTrapAccessListDeny,
       "snTrapMacFilterDeny": snTrapMacFilterDeny,
       "snTrapIcmpLocalExceedBurst": snTrapIcmpLocalExceedBurst,
       "snTrapIcmpTransitExceedBurst": snTrapIcmpTransitExceedBurst,
       "snTrapTcpLocalExceedBurst": snTrapTcpLocalExceedBurst,
       "snTrapTcpTransitExceedBurst": snTrapTcpTransitExceedBurst,
       "snTrapDuplicateIp": snTrapDuplicateIp,
       "snTrapMplsProblem": snTrapMplsProblem,
       "snTrapMplsException": snTrapMplsException,
       "snTrapMplsAudit": snTrapMplsAudit,
       "snTrapMplsDeveloper": snTrapMplsDeveloper,
       "snTrapNoBmFreeQueue": snTrapNoBmFreeQueue,
       "snTrapSmcDmaDrop": snTrapSmcDmaDrop,
       "snTrapSmcBpDrop": snTrapSmcBpDrop,
       "snTrapBmWriteSeqDrop": snTrapBmWriteSeqDrop,
       "snTrapRunningConfigChanged": snTrapRunningConfigChanged,
       "snTrapStartupConfigChanged": snTrapStartupConfigChanged,
       "snTrapUserLogin": snTrapUserLogin,
       "snTrapUserLogout": snTrapUserLogout,
       "snTrapPortSecurityViolation": snTrapPortSecurityViolation,
       "snTrapPortSecurityShutdown": snTrapPortSecurityShutdown,
       "snTrapMrpStateChange": snTrapMrpStateChange,
       "snTrapMrpCamError": snTrapMrpCamError,
       "snTrapChasPwrSupplyOK": snTrapChasPwrSupplyOK,
       "snTrapVrrpeIfStateChange": snTrapVrrpeIfStateChange,
       "snTrapVsrpIfStateChange": snTrapVsrpIfStateChange,
       "snTrapSrcIpAddressViolation": snTrapSrcIpAddressViolation,
       "snTrapClientLoginReject": snTrapClientLoginReject,
       "snTrapLocalUserConfigChange": snTrapLocalUserConfigChange,
       "snTrapVlanConfigChange": snTrapVlanConfigChange,
       "snTrapAclConfigChange": snTrapAclConfigChange,
       "snTrapMacFilterConfigChange": snTrapMacFilterConfigChange,
       "snTrapSNMPConfigChange": snTrapSNMPConfigChange,
       "snTrapSyslogConfigChange": snTrapSyslogConfigChange,
       "snTrapPasswordConfigChange": snTrapPasswordConfigChange,
       "snTrapServerStatusChange": snTrapServerStatusChange,
       "snTrapDot1xSecurityViolation": snTrapDot1xSecurityViolation,
       "snTrapDot1xPortLinkChange": snTrapDot1xPortLinkChange,
       "snTrapDot1xPortControlChange": snTrapDot1xPortControlChange,
       "snTrapDot1xVlanIdChange": snTrapDot1xVlanIdChange,
       "snTrapDot1xFilterSetupFailure": snTrapDot1xFilterSetupFailure,
       "snTrapDot1xError": snTrapDot1xError,
       "snTrapPortConfigChange": snTrapPortConfigChange,
       "snTrapMacAuthVlanIdChange": snTrapMacAuthVlanIdChange,
       "snTrapUDLDLinkDown": snTrapUDLDLinkDown,
       "snTrapUDLDLinkUp": snTrapUDLDLinkUp,
       "snTrapStpRootGuardDetect": snTrapStpRootGuardDetect,
       "snTrapStpRootGuardExpire": snTrapStpRootGuardExpire,
       "snTrapStpBPDUGuardDetect": snTrapStpBPDUGuardDetect,
       "snTrapLACPLinkStateChange": snTrapLACPLinkStateChange,
       "snTrapOpticalMonitoringNotFoundryOptics": snTrapOpticalMonitoringNotFoundryOptics,
       "snTrapOpticalMonitoringFoundryOpticsNotCapable": snTrapOpticalMonitoringFoundryOpticsNotCapable,
       "snTrapSTPBPDUGuardExpire": snTrapSTPBPDUGuardExpire,
       "snTrapIfIndexAssignmentChanged": snTrapIfIndexAssignmentChanged,
       "snTrapPBRConfigChanged": snTrapPBRConfigChanged,
       "snTrapModuleStatusChange": snTrapModuleStatusChange,
       "snTrapChasHighSpeedFansNeeded": snTrapChasHighSpeedFansNeeded,
       "snTrapSysmaxReverted": snTrapSysmaxReverted,
       "snTrapSysmaxLeftLowMem": snTrapSysmaxLeftLowMem,
       "snTrapSysMemoryLowThreshold": snTrapSysMemoryLowThreshold,
       "snTrapSysMemoryOutThreshold": snTrapSysMemoryOutThreshold,
       "snTrapChasFanOK": snTrapChasFanOK,
       "snTrapTemperatureOK": snTrapTemperatureOK,
       "snTrapCAMOverflow": snTrapCAMOverflow,
       "snTrapOpticalMonitoringWarning": snTrapOpticalMonitoringWarning,
       "snTrapOpticalMonitoringAlarm": snTrapOpticalMonitoringAlarm,
       "snTrapOpticalMonitoringError": snTrapOpticalMonitoringError,
       "snTrapPosMonitoringWarning": snTrapPosMonitoringWarning,
       "snTrapPosMonitoringAlarm": snTrapPosMonitoringAlarm,
       "snTrapPosMonitoringError": snTrapPosMonitoringError,
       "snTrapXfpSfpIncompatibleOptics": snTrapXfpSfpIncompatibleOptics,
       "snTrapTMLoggingStart": snTrapTMLoggingStart,
       "snTrapTMLoggingStop": snTrapTMLoggingStop,
       "snTrapTMLoggingRestart": snTrapTMLoggingRestart,
       "snTrapXfpSfpNotFoundryOptics": snTrapXfpSfpNotFoundryOptics,
       "snTrapTMRecoverySlotReset": snTrapTMRecoverySlotReset,
       "snTrapSFMLinkDown": snTrapSFMLinkDown,
       "snTrapSFMLinkUp": snTrapSFMLinkUp,
       "snTrapChassisFanSpeedLow": snTrapChassisFanSpeedLow,
       "snTrapChassisFanSpeedMedium": snTrapChassisFanSpeedMedium,
       "snTrapChassisFanSpeedMedHigh": snTrapChassisFanSpeedMedHigh,
       "snTrapChassisFanSpeedHigh": snTrapChassisFanSpeedHigh}
)
