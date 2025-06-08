# SNMP MIB module (CISCO-LWAPP-CLOUD-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-CLOUD-SERVICES-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:55:04 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappCloudServicesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 838)
)
if mibBuilder.loadTexts:
    ciscoLwappCloudServicesMIB.setRevisions(
        ("2018-07-03 00:00",
         "2018-04-24 00:00",
         "2017-12-21 00:00",
         "2017-02-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ClCSMIBNotifs_ObjectIdentity = ObjectIdentity
clCSMIBNotifs = _ClCSMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 0)
)
_ClCSNANotifs_ObjectIdentity = ObjectIdentity
clCSNANotifs = _ClCSNANotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 0, 0)
)
_ClCSSecTunNotifs_ObjectIdentity = ObjectIdentity
clCSSecTunNotifs = _ClCSSecTunNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 0, 1)
)
_ClCSMIBObjects_ObjectIdentity = ObjectIdentity
clCSMIBObjects = _ClCSMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1)
)
_ClCSNAObjects_ObjectIdentity = ObjectIdentity
clCSNAObjects = _ClCSNAObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1)
)
_ClCSNAServerConfig_ObjectIdentity = ObjectIdentity
clCSNAServerConfig = _ClCSNAServerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 1)
)


class _ClCSNAServerUrl_Type(SnmpAdminString):
    """Custom type clCSNAServerUrl based on SnmpAdminString"""
    defaultValue = OctetString("")


_ClCSNAServerUrl_Type.__name__ = "SnmpAdminString"
_ClCSNAServerUrl_Object = MibScalar
clCSNAServerUrl = _ClCSNAServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 1, 1),
    _ClCSNAServerUrl_Type()
)
clCSNAServerUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSNAServerUrl.setStatus("current")


class _ClCSNAServerIdToken_Type(SnmpAdminString):
    """Custom type clCSNAServerIdToken based on SnmpAdminString"""
    defaultValue = OctetString("")


_ClCSNAServerIdToken_Type.__name__ = "SnmpAdminString"
_ClCSNAServerIdToken_Object = MibScalar
clCSNAServerIdToken = _ClCSNAServerIdToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 1, 2),
    _ClCSNAServerIdToken_Type()
)
clCSNAServerIdToken.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSNAServerIdToken.setStatus("current")


class _ClCSNAServerOnchangeEnable_Type(TruthValue):
    """Custom type clCSNAServerOnchangeEnable based on TruthValue"""
    defaultValue = 2


_ClCSNAServerOnchangeEnable_Type.__name__ = "TruthValue"
_ClCSNAServerOnchangeEnable_Object = MibScalar
clCSNAServerOnchangeEnable = _ClCSNAServerOnchangeEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 1, 3),
    _ClCSNAServerOnchangeEnable_Type()
)
clCSNAServerOnchangeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSNAServerOnchangeEnable.setStatus("deprecated")


class _ClCSNAServerSyncInterval_Type(Integer32):
    """Custom type clCSNAServerSyncInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("adaptive", 2))
    )


_ClCSNAServerSyncInterval_Type.__name__ = "Integer32"
_ClCSNAServerSyncInterval_Object = MibScalar
clCSNAServerSyncInterval = _ClCSNAServerSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 1, 4),
    _ClCSNAServerSyncInterval_Type()
)
clCSNAServerSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSNAServerSyncInterval.setStatus("deprecated")


class _ClCSNAServerSubscriptionAction_Type(Integer32):
    """Custom type clCSNAServerSubscriptionAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("remove", 2))
    )


_ClCSNAServerSubscriptionAction_Type.__name__ = "Integer32"
_ClCSNAServerSubscriptionAction_Object = MibScalar
clCSNAServerSubscriptionAction = _ClCSNAServerSubscriptionAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 1, 5),
    _ClCSNAServerSubscriptionAction_Type()
)
clCSNAServerSubscriptionAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSNAServerSubscriptionAction.setStatus("deprecated")


class _ClCSNAServerSubscriptionTopic_Type(Bits):
    """Custom type clCSNAServerSubscriptionTopic based on Bits"""
    namedValues = NamedValues(
        *(("system", 0),
          ("network", 1),
          ("client", 2),
          ("ap", 3),
          ("rogue", 4),
          ("interferer", 5),
          ("apEvent", 6),
          ("clientEvent", 7),
          ("scanReport", 8),
          ("clientDnsReport", 9),
          ("fra", 10),
          ("mapserver", 11))
    )

_ClCSNAServerSubscriptionTopic_Type.__name__ = "Bits"
_ClCSNAServerSubscriptionTopic_Object = MibScalar
clCSNAServerSubscriptionTopic = _ClCSNAServerSubscriptionTopic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 1, 6),
    _ClCSNAServerSubscriptionTopic_Type()
)
clCSNAServerSubscriptionTopic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSNAServerSubscriptionTopic.setStatus("deprecated")


class _CLCSNAServerResetSubscriptions_Type(TruthValue):
    """Custom type cLCSNAServerResetSubscriptions based on TruthValue"""
    defaultValue = 2


_CLCSNAServerResetSubscriptions_Type.__name__ = "TruthValue"
_CLCSNAServerResetSubscriptions_Object = MibScalar
cLCSNAServerResetSubscriptions = _CLCSNAServerResetSubscriptions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 1, 7),
    _CLCSNAServerResetSubscriptions_Type()
)
cLCSNAServerResetSubscriptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLCSNAServerResetSubscriptions.setStatus("current")
_ClCSNAGlobalConfig_ObjectIdentity = ObjectIdentity
clCSNAGlobalConfig = _ClCSNAGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 2)
)


class _ClCSNAEnable_Type(TruthValue):
    """Custom type clCSNAEnable based on TruthValue"""
    defaultValue = 1


_ClCSNAEnable_Type.__name__ = "TruthValue"
_ClCSNAEnable_Object = MibScalar
clCSNAEnable = _ClCSNAEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 2, 1),
    _ClCSNAEnable_Type()
)
clCSNAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSNAEnable.setStatus("current")


class _ClCSNASensorBackhaulSSID_Type(SnmpAdminString):
    """Custom type clCSNASensorBackhaulSSID based on SnmpAdminString"""
    defaultValue = OctetString("")


_ClCSNASensorBackhaulSSID_Type.__name__ = "SnmpAdminString"
_ClCSNASensorBackhaulSSID_Object = MibScalar
clCSNASensorBackhaulSSID = _ClCSNASensorBackhaulSSID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 2, 2),
    _ClCSNASensorBackhaulSSID_Type()
)
clCSNASensorBackhaulSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSNASensorBackhaulSSID.setStatus("current")


class _ClCSNASensorBackhaulAuthType_Type(Integer32):
    """Custom type clCSNASensorBackhaulAuthType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot1x", 1),
          ("psk", 2),
          ("open", 3))
    )


_ClCSNASensorBackhaulAuthType_Type.__name__ = "Integer32"
_ClCSNASensorBackhaulAuthType_Object = MibScalar
clCSNASensorBackhaulAuthType = _ClCSNASensorBackhaulAuthType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 2, 3),
    _ClCSNASensorBackhaulAuthType_Type()
)
clCSNASensorBackhaulAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSNASensorBackhaulAuthType.setStatus("current")


class _ClCSNASensorBackhaulEapType_Type(Integer32):
    """Custom type clCSNASensorBackhaulEapType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eapfast", 1),
          ("peap", 2),
          ("none", 3))
    )


_ClCSNASensorBackhaulEapType_Type.__name__ = "Integer32"
_ClCSNASensorBackhaulEapType_Object = MibScalar
clCSNASensorBackhaulEapType = _ClCSNASensorBackhaulEapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 2, 4),
    _ClCSNASensorBackhaulEapType_Type()
)
clCSNASensorBackhaulEapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSNASensorBackhaulEapType.setStatus("current")


class _ClCSNASensorBackhaulUsername_Type(SnmpAdminString):
    """Custom type clCSNASensorBackhaulUsername based on SnmpAdminString"""
    defaultValue = OctetString("")


_ClCSNASensorBackhaulUsername_Type.__name__ = "SnmpAdminString"
_ClCSNASensorBackhaulUsername_Object = MibScalar
clCSNASensorBackhaulUsername = _ClCSNASensorBackhaulUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 2, 5),
    _ClCSNASensorBackhaulUsername_Type()
)
clCSNASensorBackhaulUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSNASensorBackhaulUsername.setStatus("current")


class _ClCSNASensorBackhaulPassword_Type(SnmpAdminString):
    """Custom type clCSNASensorBackhaulPassword based on SnmpAdminString"""
    defaultValue = OctetString("")


_ClCSNASensorBackhaulPassword_Type.__name__ = "SnmpAdminString"
_ClCSNASensorBackhaulPassword_Object = MibScalar
clCSNASensorBackhaulPassword = _ClCSNASensorBackhaulPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 2, 6),
    _ClCSNASensorBackhaulPassword_Type()
)
clCSNASensorBackhaulPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSNASensorBackhaulPassword.setStatus("current")


class _ClCSNASensorBackhaulPskMode_Type(Integer32):
    """Custom type clCSNASensorBackhaulPskMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("hex", 2))
    )


_ClCSNASensorBackhaulPskMode_Type.__name__ = "Integer32"
_ClCSNASensorBackhaulPskMode_Object = MibScalar
clCSNASensorBackhaulPskMode = _ClCSNASensorBackhaulPskMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 2, 7),
    _ClCSNASensorBackhaulPskMode_Type()
)
clCSNASensorBackhaulPskMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSNASensorBackhaulPskMode.setStatus("current")


class _ClCSNASensorBackhaulPsk_Type(SnmpAdminString):
    """Custom type clCSNASensorBackhaulPsk based on SnmpAdminString"""
    defaultValue = OctetString("")


_ClCSNASensorBackhaulPsk_Type.__name__ = "SnmpAdminString"
_ClCSNASensorBackhaulPsk_Object = MibScalar
clCSNASensorBackhaulPsk = _ClCSNASensorBackhaulPsk_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 2, 8),
    _ClCSNASensorBackhaulPsk_Type()
)
clCSNASensorBackhaulPsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSNASensorBackhaulPsk.setStatus("current")


class _ClCSNAASIEnable_Type(TruthValue):
    """Custom type clCSNAASIEnable based on TruthValue"""
    defaultValue = 2


_ClCSNAASIEnable_Type.__name__ = "TruthValue"
_ClCSNAASIEnable_Object = MibScalar
clCSNAASIEnable = _ClCSNAASIEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 2, 9),
    _ClCSNAASIEnable_Type()
)
clCSNAASIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSNAASIEnable.setStatus("deprecated")


class _ClCSNADiffSyncEnable_Type(TruthValue):
    """Custom type clCSNADiffSyncEnable based on TruthValue"""
    defaultValue = 2


_ClCSNADiffSyncEnable_Type.__name__ = "TruthValue"
_ClCSNADiffSyncEnable_Object = MibScalar
clCSNADiffSyncEnable = _ClCSNADiffSyncEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 2, 10),
    _ClCSNADiffSyncEnable_Type()
)
clCSNADiffSyncEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSNADiffSyncEnable.setStatus("deprecated")
_ClCSNATrapMgmtObjects_ObjectIdentity = ObjectIdentity
clCSNATrapMgmtObjects = _ClCSNATrapMgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 3)
)
_ClCSNASensorLradMacAddr_Type = MacAddress
_ClCSNASensorLradMacAddr_Object = MibScalar
clCSNASensorLradMacAddr = _ClCSNASensorLradMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 3, 1),
    _ClCSNASensorLradMacAddr_Type()
)
clCSNASensorLradMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clCSNASensorLradMacAddr.setStatus("current")


class _ClCSNASensorStatus_Type(Integer32):
    """Custom type clCSNASensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("wsaNoUpdate", 1),
          ("wsaStatusOk", 2),
          ("wsaServerUrlNotReachable", 3),
          ("wsaServerwrongIdToken", 4),
          ("wsaServerProxyNotReachable", 5),
          ("wsaSensorIntf24Error", 6),
          ("wsaSensorIntf24ProxyError", 7),
          ("wsaSensorIntf50Error", 8),
          ("wsaSensorIntf50ProxyError", 9),
          ("wsaApLicenseDenied", 10),
          ("wsaNAServerUnreachable", 11),
          ("wsaAttemptAssocToRoot", 12),
          ("wsaAssocToRoot", 13),
          ("wsaTestCfgRcvd", 14),
          ("wsaStatusmax", 15))
    )


_ClCSNASensorStatus_Type.__name__ = "Integer32"
_ClCSNASensorStatus_Object = MibScalar
clCSNASensorStatus = _ClCSNASensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 3, 2),
    _ClCSNASensorStatus_Type()
)
clCSNASensorStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clCSNASensorStatus.setStatus("current")


class _ClCSNASensorErrCode_Type(Integer32):
    """Custom type clCSNASensorErrCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("wsaSensorBackhaulWronSsid", 1),
          ("wsaSensorBackhaulInvalidCredential", 2),
          ("wsaSensorConnError", 3),
          ("wsaNAServerNotFound", 4),
          ("wsaNAServerInternalError", 5))
    )


_ClCSNASensorErrCode_Type.__name__ = "Integer32"
_ClCSNASensorErrCode_Object = MibScalar
clCSNASensorErrCode = _ClCSNASensorErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 3, 3),
    _ClCSNASensorErrCode_Type()
)
clCSNASensorErrCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clCSNASensorErrCode.setStatus("current")
_ClCSNAServerConfigTable_ObjectIdentity = ObjectIdentity
clCSNAServerConfigTable = _ClCSNAServerConfigTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 4)
)
_CLCSNAServerChannelTable_Object = MibTable
cLCSNAServerChannelTable = _CLCSNAServerChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cLCSNAServerChannelTable.setStatus("current")
_CLCSNAServerChannelEntry_Object = MibTableRow
cLCSNAServerChannelEntry = _CLCSNAServerChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 4, 1, 1)
)
cLCSNAServerChannelEntry.setIndexNames(
    (0, "CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNAServerChannelName"),
)
if mibBuilder.loadTexts:
    cLCSNAServerChannelEntry.setStatus("current")
_ClCSNAServerChannelName_Type = SnmpAdminString
_ClCSNAServerChannelName_Object = MibTableColumn
clCSNAServerChannelName = _ClCSNAServerChannelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 4, 1, 1, 1),
    _ClCSNAServerChannelName_Type()
)
clCSNAServerChannelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clCSNAServerChannelName.setStatus("current")


class _ClCSNAServerChannelSyncInterval_Type(Integer32):
    """Custom type clCSNAServerChannelSyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(15,
              30,
              60,
              300)
        )
    )
    namedValues = NamedValues(
        *(("fifteen", 15),
          ("thirty", 30),
          ("sixty", 60),
          ("threehundred", 300))
    )


_ClCSNAServerChannelSyncInterval_Type.__name__ = "Integer32"
_ClCSNAServerChannelSyncInterval_Object = MibTableColumn
clCSNAServerChannelSyncInterval = _ClCSNAServerChannelSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 4, 1, 1, 2),
    _ClCSNAServerChannelSyncInterval_Type()
)
clCSNAServerChannelSyncInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clCSNAServerChannelSyncInterval.setStatus("current")
if mibBuilder.loadTexts:
    clCSNAServerChannelSyncInterval.setUnits("Seconds")
_ClCSNAServerChannelOnChangeMode_Type = TruthValue
_ClCSNAServerChannelOnChangeMode_Object = MibTableColumn
clCSNAServerChannelOnChangeMode = _ClCSNAServerChannelOnChangeMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 4, 1, 1, 3),
    _ClCSNAServerChannelOnChangeMode_Type()
)
clCSNAServerChannelOnChangeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clCSNAServerChannelOnChangeMode.setStatus("current")


class _ClCSNAServerIsFilterChannel_Type(TruthValue):
    """Custom type clCSNAServerIsFilterChannel based on TruthValue"""
    defaultValue = 2


_ClCSNAServerIsFilterChannel_Type.__name__ = "TruthValue"
_ClCSNAServerIsFilterChannel_Object = MibTableColumn
clCSNAServerIsFilterChannel = _ClCSNAServerIsFilterChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 4, 1, 1, 4),
    _ClCSNAServerIsFilterChannel_Type()
)
clCSNAServerIsFilterChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clCSNAServerIsFilterChannel.setStatus("current")
_ClCSNAServerChannelRowStatus_Type = RowStatus
_ClCSNAServerChannelRowStatus_Object = MibTableColumn
clCSNAServerChannelRowStatus = _ClCSNAServerChannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 1, 4, 1, 1, 5),
    _ClCSNAServerChannelRowStatus_Type()
)
clCSNAServerChannelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clCSNAServerChannelRowStatus.setStatus("current")
_ClCSDXObjects_ObjectIdentity = ObjectIdentity
clCSDXObjects = _ClCSDXObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 2)
)
_ClCSDxConfig_ObjectIdentity = ObjectIdentity
clCSDxConfig = _ClCSDxConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 2, 1)
)


class _ClCSDxMode_Type(TruthValue):
    """Custom type clCSDxMode based on TruthValue"""
    defaultValue = 2


_ClCSDxMode_Type.__name__ = "TruthValue"
_ClCSDxMode_Object = MibScalar
clCSDxMode = _ClCSDxMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 2, 1, 1),
    _ClCSDxMode_Type()
)
clCSDxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSDxMode.setStatus("current")
_ClCSCMXObjects_ObjectIdentity = ObjectIdentity
clCSCMXObjects = _ClCSCMXObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 3)
)
_ClCSCMXServerConfig_ObjectIdentity = ObjectIdentity
clCSCMXServerConfig = _ClCSCMXServerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 3, 1)
)


class _ClCSCMXServerUrl_Type(SnmpAdminString):
    """Custom type clCSCMXServerUrl based on SnmpAdminString"""
    defaultValue = OctetString("")


_ClCSCMXServerUrl_Type.__name__ = "SnmpAdminString"
_ClCSCMXServerUrl_Object = MibScalar
clCSCMXServerUrl = _ClCSCMXServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 3, 1, 1),
    _ClCSCMXServerUrl_Type()
)
clCSCMXServerUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSCMXServerUrl.setStatus("current")


class _ClCSCMXServerIdToken_Type(SnmpAdminString):
    """Custom type clCSCMXServerIdToken based on SnmpAdminString"""
    defaultValue = OctetString("")


_ClCSCMXServerIdToken_Type.__name__ = "SnmpAdminString"
_ClCSCMXServerIdToken_Object = MibScalar
clCSCMXServerIdToken = _ClCSCMXServerIdToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 3, 1, 2),
    _ClCSCMXServerIdToken_Type()
)
clCSCMXServerIdToken.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSCMXServerIdToken.setStatus("current")
_ClCSCMXConfig_ObjectIdentity = ObjectIdentity
clCSCMXConfig = _ClCSCMXConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 3, 2)
)


class _ClCSCMXEnable_Type(TruthValue):
    """Custom type clCSCMXEnable based on TruthValue"""
    defaultValue = 2


_ClCSCMXEnable_Type.__name__ = "TruthValue"
_ClCSCMXEnable_Object = MibScalar
clCSCMXEnable = _ClCSCMXEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 3, 2, 1),
    _ClCSCMXEnable_Type()
)
clCSCMXEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSCMXEnable.setStatus("current")


class _ClCSCMXOnPremisesEnable_Type(TruthValue):
    """Custom type clCSCMXOnPremisesEnable based on TruthValue"""
    defaultValue = 1


_ClCSCMXOnPremisesEnable_Type.__name__ = "TruthValue"
_ClCSCMXOnPremisesEnable_Object = MibScalar
clCSCMXOnPremisesEnable = _ClCSCMXOnPremisesEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 3, 2, 2),
    _ClCSCMXOnPremisesEnable_Type()
)
clCSCMXOnPremisesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSCMXOnPremisesEnable.setStatus("current")
_ClCSSecTunObjects_ObjectIdentity = ObjectIdentity
clCSSecTunObjects = _ClCSSecTunObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4)
)
_ClCSSecTunConfig_ObjectIdentity = ObjectIdentity
clCSSecTunConfig = _ClCSSecTunConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 1)
)


class _ClCSSecTunEnable_Type(TruthValue):
    """Custom type clCSSecTunEnable based on TruthValue"""
    defaultValue = 2


_ClCSSecTunEnable_Type.__name__ = "TruthValue"
_ClCSSecTunEnable_Object = MibScalar
clCSSecTunEnable = _ClCSSecTunEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 1, 1),
    _ClCSSecTunEnable_Type()
)
clCSSecTunEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSSecTunEnable.setStatus("current")


class _ClCSSecTunTlsGwFqdn_Type(SnmpAdminString):
    """Custom type clCSSecTunTlsGwFqdn based on SnmpAdminString"""
    defaultValue = OctetString("")


_ClCSSecTunTlsGwFqdn_Type.__name__ = "SnmpAdminString"
_ClCSSecTunTlsGwFqdn_Object = MibScalar
clCSSecTunTlsGwFqdn = _ClCSSecTunTlsGwFqdn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 1, 2),
    _ClCSSecTunTlsGwFqdn_Type()
)
clCSSecTunTlsGwFqdn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSSecTunTlsGwFqdn.setStatus("current")
_ClCSSecTunTlsGwIpAddrType_Type = InetAddressType
_ClCSSecTunTlsGwIpAddrType_Object = MibScalar
clCSSecTunTlsGwIpAddrType = _ClCSSecTunTlsGwIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 1, 3),
    _ClCSSecTunTlsGwIpAddrType_Type()
)
clCSSecTunTlsGwIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSSecTunTlsGwIpAddrType.setStatus("current")
_ClCSSecTunTlsGwIpAddr_Type = InetAddress
_ClCSSecTunTlsGwIpAddr_Object = MibScalar
clCSSecTunTlsGwIpAddr = _ClCSSecTunTlsGwIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 1, 4),
    _ClCSSecTunTlsGwIpAddr_Type()
)
clCSSecTunTlsGwIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSSecTunTlsGwIpAddr.setStatus("current")


class _ClCSSecTunTlsGwPort_Type(InetPortNumber):
    """Custom type clCSSecTunTlsGwPort based on InetPortNumber"""
    defaultValue = 0


_ClCSSecTunTlsGwPort_Type.__name__ = "InetPortNumber"
_ClCSSecTunTlsGwPort_Object = MibScalar
clCSSecTunTlsGwPort = _ClCSSecTunTlsGwPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 1, 5),
    _ClCSSecTunTlsGwPort_Type()
)
clCSSecTunTlsGwPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSSecTunTlsGwPort.setStatus("current")


class _ClCSSecTunPskId_Type(SnmpAdminString):
    """Custom type clCSSecTunPskId based on SnmpAdminString"""
    defaultValue = OctetString("")


_ClCSSecTunPskId_Type.__name__ = "SnmpAdminString"
_ClCSSecTunPskId_Object = MibScalar
clCSSecTunPskId = _ClCSSecTunPskId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 1, 6),
    _ClCSSecTunPskId_Type()
)
clCSSecTunPskId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSSecTunPskId.setStatus("current")


class _ClCSSecTunPskKey_Type(SnmpAdminString):
    """Custom type clCSSecTunPskKey based on SnmpAdminString"""
    defaultValue = OctetString("")


_ClCSSecTunPskKey_Type.__name__ = "SnmpAdminString"
_ClCSSecTunPskKey_Object = MibScalar
clCSSecTunPskKey = _ClCSSecTunPskKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 1, 7),
    _ClCSSecTunPskKey_Type()
)
clCSSecTunPskKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSSecTunPskKey.setStatus("current")


class _ClCSSecTunRadiusEnable_Type(TruthValue):
    """Custom type clCSSecTunRadiusEnable based on TruthValue"""
    defaultValue = 2


_ClCSSecTunRadiusEnable_Type.__name__ = "TruthValue"
_ClCSSecTunRadiusEnable_Object = MibScalar
clCSSecTunRadiusEnable = _ClCSSecTunRadiusEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 1, 8),
    _ClCSSecTunRadiusEnable_Type()
)
clCSSecTunRadiusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSSecTunRadiusEnable.setStatus("current")


class _ClCSSecTunSnmpTrapEnable_Type(TruthValue):
    """Custom type clCSSecTunSnmpTrapEnable based on TruthValue"""
    defaultValue = 2


_ClCSSecTunSnmpTrapEnable_Type.__name__ = "TruthValue"
_ClCSSecTunSnmpTrapEnable_Object = MibScalar
clCSSecTunSnmpTrapEnable = _ClCSSecTunSnmpTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 1, 9),
    _ClCSSecTunSnmpTrapEnable_Type()
)
clCSSecTunSnmpTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSSecTunSnmpTrapEnable.setStatus("current")
_CLCSSecTunStaticNetworkTable_Object = MibTable
cLCSSecTunStaticNetworkTable = _CLCSSecTunStaticNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 1, 10)
)
if mibBuilder.loadTexts:
    cLCSSecTunStaticNetworkTable.setStatus("current")
_CLCSSecTunStaticNetworkEntry_Object = MibTableRow
cLCSSecTunStaticNetworkEntry = _CLCSSecTunStaticNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 1, 10, 1)
)
cLCSSecTunStaticNetworkEntry.setIndexNames(
    (0, "CISCO-LWAPP-CLOUD-SERVICES-MIB", "cLSCSecTunNetworkIPAddressType"),
    (0, "CISCO-LWAPP-CLOUD-SERVICES-MIB", "cLSCSecTunNetworkIPAddress"),
    (0, "CISCO-LWAPP-CLOUD-SERVICES-MIB", "cLSCSecTunNetworkIPNetmaskType"),
    (0, "CISCO-LWAPP-CLOUD-SERVICES-MIB", "cLSCSecTunNetworkIPNetmask"),
)
if mibBuilder.loadTexts:
    cLCSSecTunStaticNetworkEntry.setStatus("current")
_CLSCSecTunNetworkIPAddressType_Type = InetAddressType
_CLSCSecTunNetworkIPAddressType_Object = MibTableColumn
cLSCSecTunNetworkIPAddressType = _CLSCSecTunNetworkIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 1, 10, 1, 1),
    _CLSCSecTunNetworkIPAddressType_Type()
)
cLSCSecTunNetworkIPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLSCSecTunNetworkIPAddressType.setStatus("current")
_CLSCSecTunNetworkIPAddress_Type = InetAddress
_CLSCSecTunNetworkIPAddress_Object = MibTableColumn
cLSCSecTunNetworkIPAddress = _CLSCSecTunNetworkIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 1, 10, 1, 2),
    _CLSCSecTunNetworkIPAddress_Type()
)
cLSCSecTunNetworkIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLSCSecTunNetworkIPAddress.setStatus("current")
_CLSCSecTunNetworkIPNetmaskType_Type = InetAddressType
_CLSCSecTunNetworkIPNetmaskType_Object = MibTableColumn
cLSCSecTunNetworkIPNetmaskType = _CLSCSecTunNetworkIPNetmaskType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 1, 10, 1, 3),
    _CLSCSecTunNetworkIPNetmaskType_Type()
)
cLSCSecTunNetworkIPNetmaskType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLSCSecTunNetworkIPNetmaskType.setStatus("current")
_CLSCSecTunNetworkIPNetmask_Type = InetAddress
_CLSCSecTunNetworkIPNetmask_Object = MibTableColumn
cLSCSecTunNetworkIPNetmask = _CLSCSecTunNetworkIPNetmask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 1, 10, 1, 4),
    _CLSCSecTunNetworkIPNetmask_Type()
)
cLSCSecTunNetworkIPNetmask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLSCSecTunNetworkIPNetmask.setStatus("current")
_CLSCSecTunNetworkRowStatus_Type = RowStatus
_CLSCSecTunNetworkRowStatus_Object = MibTableColumn
cLSCSecTunNetworkRowStatus = _CLSCSecTunNetworkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 1, 10, 1, 5),
    _CLSCSecTunNetworkRowStatus_Type()
)
cLSCSecTunNetworkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLSCSecTunNetworkRowStatus.setStatus("current")
_ClCSSecTunInfo_ObjectIdentity = ObjectIdentity
clCSSecTunInfo = _ClCSSecTunInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 2)
)


class _ClCSSecTunCurrentState_Type(Integer32):
    """Custom type clCSSecTunCurrentState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("secureTunnelDown", 1),
          ("secureTunnelUp", 2))
    )


_ClCSSecTunCurrentState_Type.__name__ = "Integer32"
_ClCSSecTunCurrentState_Object = MibScalar
clCSSecTunCurrentState = _ClCSSecTunCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 2, 1),
    _ClCSSecTunCurrentState_Type()
)
clCSSecTunCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clCSSecTunCurrentState.setStatus("current")
_ClCSSecTunTlsGwIpAddrInUseType_Type = InetAddressType
_ClCSSecTunTlsGwIpAddrInUseType_Object = MibScalar
clCSSecTunTlsGwIpAddrInUseType = _ClCSSecTunTlsGwIpAddrInUseType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 2, 2),
    _ClCSSecTunTlsGwIpAddrInUseType_Type()
)
clCSSecTunTlsGwIpAddrInUseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clCSSecTunTlsGwIpAddrInUseType.setStatus("current")
_ClCSSecTunTlsGwIpInUseAddr_Type = InetAddress
_ClCSSecTunTlsGwIpInUseAddr_Object = MibScalar
clCSSecTunTlsGwIpInUseAddr = _ClCSSecTunTlsGwIpInUseAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 2, 3),
    _ClCSSecTunTlsGwIpInUseAddr_Type()
)
clCSSecTunTlsGwIpInUseAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clCSSecTunTlsGwIpInUseAddr.setStatus("current")
_ClCSSecTunInnerIpAddrType_Type = InetAddressType
_ClCSSecTunInnerIpAddrType_Object = MibScalar
clCSSecTunInnerIpAddrType = _ClCSSecTunInnerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 2, 4),
    _ClCSSecTunInnerIpAddrType_Type()
)
clCSSecTunInnerIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clCSSecTunInnerIpAddrType.setStatus("current")
_ClCSSecTunInnerIpAddr_Type = InetAddress
_ClCSSecTunInnerIpAddr_Object = MibScalar
clCSSecTunInnerIpAddr = _ClCSSecTunInnerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 2, 5),
    _ClCSSecTunInnerIpAddr_Type()
)
clCSSecTunInnerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clCSSecTunInnerIpAddr.setStatus("current")


class _ClCSSecTunTLSClientProcState_Type(Integer32):
    """Custom type clCSSecTunTLSClientProcState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("tlscProcDown", 1),
          ("tlscProcInProg", 2),
          ("tlscProcUp", 3),
          ("tlscProcReStart", 4))
    )


_ClCSSecTunTLSClientProcState_Type.__name__ = "Integer32"
_ClCSSecTunTLSClientProcState_Object = MibScalar
clCSSecTunTLSClientProcState = _ClCSSecTunTLSClientProcState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 2, 6),
    _ClCSSecTunTLSClientProcState_Type()
)
clCSSecTunTLSClientProcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clCSSecTunTLSClientProcState.setStatus("current")
_CLCSSecTunRouteTable_Object = MibTable
cLCSSecTunRouteTable = _CLCSSecTunRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 2, 7)
)
if mibBuilder.loadTexts:
    cLCSSecTunRouteTable.setStatus("current")
_CLCSSecTunRouteEntry_Object = MibTableRow
cLCSSecTunRouteEntry = _CLCSSecTunRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 2, 7, 1)
)
cLCSSecTunRouteEntry.setIndexNames(
    (0, "CISCO-LWAPP-CLOUD-SERVICES-MIB", "cLSCSecTunRouteIPAddressType"),
    (0, "CISCO-LWAPP-CLOUD-SERVICES-MIB", "cLSCSecTunRouteIPAddress"),
    (0, "CISCO-LWAPP-CLOUD-SERVICES-MIB", "cLSCSecTunRouteNetmaskType"),
    (0, "CISCO-LWAPP-CLOUD-SERVICES-MIB", "cLSCSecTunRouteNetmask"),
)
if mibBuilder.loadTexts:
    cLCSSecTunRouteEntry.setStatus("current")
_CLSCSecTunRouteIPAddressType_Type = InetAddressType
_CLSCSecTunRouteIPAddressType_Object = MibTableColumn
cLSCSecTunRouteIPAddressType = _CLSCSecTunRouteIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 2, 7, 1, 1),
    _CLSCSecTunRouteIPAddressType_Type()
)
cLSCSecTunRouteIPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLSCSecTunRouteIPAddressType.setStatus("current")
_CLSCSecTunRouteIPAddress_Type = InetAddress
_CLSCSecTunRouteIPAddress_Object = MibTableColumn
cLSCSecTunRouteIPAddress = _CLSCSecTunRouteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 2, 7, 1, 2),
    _CLSCSecTunRouteIPAddress_Type()
)
cLSCSecTunRouteIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLSCSecTunRouteIPAddress.setStatus("current")
_CLSCSecTunRouteNetmaskType_Type = InetAddressType
_CLSCSecTunRouteNetmaskType_Object = MibTableColumn
cLSCSecTunRouteNetmaskType = _CLSCSecTunRouteNetmaskType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 2, 7, 1, 3),
    _CLSCSecTunRouteNetmaskType_Type()
)
cLSCSecTunRouteNetmaskType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLSCSecTunRouteNetmaskType.setStatus("current")
_CLSCSecTunRouteNetmask_Type = InetAddress
_CLSCSecTunRouteNetmask_Object = MibTableColumn
cLSCSecTunRouteNetmask = _CLSCSecTunRouteNetmask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 2, 7, 1, 4),
    _CLSCSecTunRouteNetmask_Type()
)
cLSCSecTunRouteNetmask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLSCSecTunRouteNetmask.setStatus("current")
_CLSCSecTunRouteTableRowStatus_Type = Unsigned32
_CLSCSecTunRouteTableRowStatus_Object = MibTableColumn
cLSCSecTunRouteTableRowStatus = _CLSCSecTunRouteTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 4, 2, 7, 1, 5),
    _CLSCSecTunRouteTableRowStatus_Type()
)
cLSCSecTunRouteTableRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSCSecTunRouteTableRowStatus.setStatus("current")
_ClCSWebhookGlobalObjects_ObjectIdentity = ObjectIdentity
clCSWebhookGlobalObjects = _ClCSWebhookGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 5)
)


class _ClCSWebhookUrl_Type(SnmpAdminString):
    """Custom type clCSWebhookUrl based on SnmpAdminString"""
    defaultValue = OctetString("")


_ClCSWebhookUrl_Type.__name__ = "SnmpAdminString"
_ClCSWebhookUrl_Object = MibScalar
clCSWebhookUrl = _ClCSWebhookUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 5, 1),
    _ClCSWebhookUrl_Type()
)
clCSWebhookUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSWebhookUrl.setStatus("current")


class _ClCSWebhookAuthToken_Type(SnmpAdminString):
    """Custom type clCSWebhookAuthToken based on SnmpAdminString"""
    defaultValue = OctetString("")


_ClCSWebhookAuthToken_Type.__name__ = "SnmpAdminString"
_ClCSWebhookAuthToken_Object = MibScalar
clCSWebhookAuthToken = _ClCSWebhookAuthToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 5, 2),
    _ClCSWebhookAuthToken_Type()
)
clCSWebhookAuthToken.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSWebhookAuthToken.setStatus("current")


class _ClCSWebhookEnable_Type(TruthValue):
    """Custom type clCSWebhookEnable based on TruthValue"""
    defaultValue = 2


_ClCSWebhookEnable_Type.__name__ = "TruthValue"
_ClCSWebhookEnable_Object = MibScalar
clCSWebhookEnable = _ClCSWebhookEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 5, 3),
    _ClCSWebhookEnable_Type()
)
clCSWebhookEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSWebhookEnable.setStatus("current")


class _ClCSWebhookOnchangeEnable_Type(TruthValue):
    """Custom type clCSWebhookOnchangeEnable based on TruthValue"""
    defaultValue = 2


_ClCSWebhookOnchangeEnable_Type.__name__ = "TruthValue"
_ClCSWebhookOnchangeEnable_Object = MibScalar
clCSWebhookOnchangeEnable = _ClCSWebhookOnchangeEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 5, 4),
    _ClCSWebhookOnchangeEnable_Type()
)
clCSWebhookOnchangeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSWebhookOnchangeEnable.setStatus("deprecated")


class _ClCSWebhookSyncInterval_Type(Integer32):
    """Custom type clCSWebhookSyncInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("adaptive", 2))
    )


_ClCSWebhookSyncInterval_Type.__name__ = "Integer32"
_ClCSWebhookSyncInterval_Object = MibScalar
clCSWebhookSyncInterval = _ClCSWebhookSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 5, 5),
    _ClCSWebhookSyncInterval_Type()
)
clCSWebhookSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSWebhookSyncInterval.setStatus("deprecated")


class _ClCSWebhookSubscriptionAction_Type(Integer32):
    """Custom type clCSWebhookSubscriptionAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("remove", 2))
    )


_ClCSWebhookSubscriptionAction_Type.__name__ = "Integer32"
_ClCSWebhookSubscriptionAction_Object = MibScalar
clCSWebhookSubscriptionAction = _ClCSWebhookSubscriptionAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 5, 6),
    _ClCSWebhookSubscriptionAction_Type()
)
clCSWebhookSubscriptionAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSWebhookSubscriptionAction.setStatus("deprecated")


class _ClCSWebhookSubscriptionTopic_Type(Bits):
    """Custom type clCSWebhookSubscriptionTopic based on Bits"""
    namedValues = NamedValues(
        *(("system", 0),
          ("network", 1),
          ("client", 2),
          ("ap", 3),
          ("rogue", 4),
          ("interferer", 5),
          ("mapserver", 6))
    )

_ClCSWebhookSubscriptionTopic_Type.__name__ = "Bits"
_ClCSWebhookSubscriptionTopic_Object = MibScalar
clCSWebhookSubscriptionTopic = _ClCSWebhookSubscriptionTopic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 5, 7),
    _ClCSWebhookSubscriptionTopic_Type()
)
clCSWebhookSubscriptionTopic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCSWebhookSubscriptionTopic.setStatus("deprecated")


class _CLCSWebhookResetSubscriptions_Type(TruthValue):
    """Custom type cLCSWebhookResetSubscriptions based on TruthValue"""
    defaultValue = 2


_CLCSWebhookResetSubscriptions_Type.__name__ = "TruthValue"
_CLCSWebhookResetSubscriptions_Object = MibScalar
cLCSWebhookResetSubscriptions = _CLCSWebhookResetSubscriptions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 5, 8),
    _CLCSWebhookResetSubscriptions_Type()
)
cLCSWebhookResetSubscriptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLCSWebhookResetSubscriptions.setStatus("current")
_ClCSWebhookTableObjects_ObjectIdentity = ObjectIdentity
clCSWebhookTableObjects = _ClCSWebhookTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 6)
)
_CLCSWebhookChannelTable_Object = MibTable
cLCSWebhookChannelTable = _CLCSWebhookChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cLCSWebhookChannelTable.setStatus("current")
_CLCSWebhookChannelEntry_Object = MibTableRow
cLCSWebhookChannelEntry = _CLCSWebhookChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 6, 1, 1)
)
cLCSWebhookChannelEntry.setIndexNames(
    (0, "CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSWebhookChannelName"),
)
if mibBuilder.loadTexts:
    cLCSWebhookChannelEntry.setStatus("current")
_ClCSWebhookChannelName_Type = SnmpAdminString
_ClCSWebhookChannelName_Object = MibTableColumn
clCSWebhookChannelName = _ClCSWebhookChannelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 6, 1, 1, 1),
    _ClCSWebhookChannelName_Type()
)
clCSWebhookChannelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clCSWebhookChannelName.setStatus("current")


class _ClCSWebhookChannelSyncInterval_Type(Integer32):
    """Custom type clCSWebhookChannelSyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(15,
              30,
              60,
              300)
        )
    )
    namedValues = NamedValues(
        *(("fifteen", 15),
          ("thirty", 30),
          ("sixty", 60),
          ("threehundred", 300))
    )


_ClCSWebhookChannelSyncInterval_Type.__name__ = "Integer32"
_ClCSWebhookChannelSyncInterval_Object = MibTableColumn
clCSWebhookChannelSyncInterval = _ClCSWebhookChannelSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 6, 1, 1, 2),
    _ClCSWebhookChannelSyncInterval_Type()
)
clCSWebhookChannelSyncInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clCSWebhookChannelSyncInterval.setStatus("current")
if mibBuilder.loadTexts:
    clCSWebhookChannelSyncInterval.setUnits("Seconds")
_ClCSWebhookChannelOnChangeMode_Type = TruthValue
_ClCSWebhookChannelOnChangeMode_Object = MibTableColumn
clCSWebhookChannelOnChangeMode = _ClCSWebhookChannelOnChangeMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 6, 1, 1, 3),
    _ClCSWebhookChannelOnChangeMode_Type()
)
clCSWebhookChannelOnChangeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clCSWebhookChannelOnChangeMode.setStatus("current")
_ClCSWebhookChannelRowStatus_Type = RowStatus
_ClCSWebhookChannelRowStatus_Object = MibTableColumn
clCSWebhookChannelRowStatus = _ClCSWebhookChannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 6, 1, 1, 4),
    _ClCSWebhookChannelRowStatus_Type()
)
clCSWebhookChannelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clCSWebhookChannelRowStatus.setStatus("current")
_ClCSFilterChanTableObjects_ObjectIdentity = ObjectIdentity
clCSFilterChanTableObjects = _ClCSFilterChanTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 7)
)
_CLCSTelemetryFCTable_Object = MibTable
cLCSTelemetryFCTable = _CLCSTelemetryFCTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cLCSTelemetryFCTable.setStatus("current")
_CLCSTelemetryFCEntry_Object = MibTableRow
cLCSTelemetryFCEntry = _CLCSTelemetryFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 7, 1, 1)
)
cLCSTelemetryFCEntry.setIndexNames(
    (0, "CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSTelemetryFCName"),
)
if mibBuilder.loadTexts:
    cLCSTelemetryFCEntry.setStatus("current")
_ClCSTelemetryFCName_Type = SnmpAdminString
_ClCSTelemetryFCName_Object = MibTableColumn
clCSTelemetryFCName = _ClCSTelemetryFCName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 7, 1, 1, 1),
    _ClCSTelemetryFCName_Type()
)
clCSTelemetryFCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clCSTelemetryFCName.setStatus("current")
_ClCSTelemetryFCParent_Type = SnmpAdminString
_ClCSTelemetryFCParent_Object = MibTableColumn
clCSTelemetryFCParent = _ClCSTelemetryFCParent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 7, 1, 1, 2),
    _ClCSTelemetryFCParent_Type()
)
clCSTelemetryFCParent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clCSTelemetryFCParent.setStatus("current")


class _ClCSTelemetryFCSubStatus_Type(Integer32):
    """Custom type clCSTelemetryFCSubStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("assurance", 2),
          ("webhook", 3))
    )


_ClCSTelemetryFCSubStatus_Type.__name__ = "Integer32"
_ClCSTelemetryFCSubStatus_Object = MibTableColumn
clCSTelemetryFCSubStatus = _ClCSTelemetryFCSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 7, 1, 1, 3),
    _ClCSTelemetryFCSubStatus_Type()
)
clCSTelemetryFCSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clCSTelemetryFCSubStatus.setStatus("current")


class _ClCSTelemetryFCFilterCount_Type(Unsigned32):
    """Custom type clCSTelemetryFCFilterCount based on Unsigned32"""
    defaultValue = 0


_ClCSTelemetryFCFilterCount_Type.__name__ = "Unsigned32"
_ClCSTelemetryFCFilterCount_Object = MibTableColumn
clCSTelemetryFCFilterCount = _ClCSTelemetryFCFilterCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 7, 1, 1, 4),
    _ClCSTelemetryFCFilterCount_Type()
)
clCSTelemetryFCFilterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clCSTelemetryFCFilterCount.setStatus("current")
_ClCSTelemetryFCRowStatus_Type = RowStatus
_ClCSTelemetryFCRowStatus_Object = MibTableColumn
clCSTelemetryFCRowStatus = _ClCSTelemetryFCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 7, 1, 1, 5),
    _ClCSTelemetryFCRowStatus_Type()
)
clCSTelemetryFCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clCSTelemetryFCRowStatus.setStatus("current")
_CLCSTelemetryFCFilterTable_Object = MibTable
cLCSTelemetryFCFilterTable = _CLCSTelemetryFCFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 7, 2)
)
if mibBuilder.loadTexts:
    cLCSTelemetryFCFilterTable.setStatus("current")
_CLCSTelemetryFCFilterEntry_Object = MibTableRow
cLCSTelemetryFCFilterEntry = _CLCSTelemetryFCFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 7, 2, 1)
)
cLCSTelemetryFCFilterEntry.setIndexNames(
    (0, "CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSTelemetryFCName"),
    (0, "CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSTelemetryFCFilter"),
)
if mibBuilder.loadTexts:
    cLCSTelemetryFCFilterEntry.setStatus("current")
_ClCSTelemetryFCFilter_Type = SnmpAdminString
_ClCSTelemetryFCFilter_Object = MibTableColumn
clCSTelemetryFCFilter = _ClCSTelemetryFCFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 7, 2, 1, 1),
    _ClCSTelemetryFCFilter_Type()
)
clCSTelemetryFCFilter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clCSTelemetryFCFilter.setStatus("current")
_ClCSTelemetryFCFilterRowStatus_Type = RowStatus
_ClCSTelemetryFCFilterRowStatus_Object = MibTableColumn
clCSTelemetryFCFilterRowStatus = _ClCSTelemetryFCFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 1, 7, 2, 1, 2),
    _ClCSTelemetryFCFilterRowStatus_Type()
)
clCSTelemetryFCFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clCSTelemetryFCFilterRowStatus.setStatus("current")
_ClCSMIBConform_ObjectIdentity = ObjectIdentity
clCSMIBConform = _ClCSMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 2)
)
_ClCSMIBCompliances_ObjectIdentity = ObjectIdentity
clCSMIBCompliances = _ClCSMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 2, 1)
)
_ClCSMIBGroups_ObjectIdentity = ObjectIdentity
clCSMIBGroups = _ClCSMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 2, 2)
)

# Managed Objects groups

clCSNAServerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 2, 2, 1)
)
clCSNAServerConfigGroup.setObjects(
      *(("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNAServerUrl"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNAServerIdToken"))
)
if mibBuilder.loadTexts:
    clCSNAServerConfigGroup.setStatus("current")

clCSNAGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 2, 2, 2)
)
clCSNAGlobalConfigGroup.setObjects(
      *(("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNAEnable"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorBackhaulSSID"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorBackhaulAuthType"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorBackhaulEapType"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorBackhaulUsername"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorBackhaulPassword"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorBackhaulPsk"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorBackhaulPskMode"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNAASIEnable"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNADiffSyncEnable"))
)
if mibBuilder.loadTexts:
    clCSNAGlobalConfigGroup.setStatus("deprecated")

clCSCMXServerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 2, 2, 3)
)
clCSCMXServerConfigGroup.setObjects(
      *(("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSCMXServerUrl"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSCMXServerIdToken"))
)
if mibBuilder.loadTexts:
    clCSCMXServerConfigGroup.setStatus("current")

clCSCMXConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 2, 2, 4)
)
clCSCMXConfigGroup.setObjects(
    ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSCMXEnable")
)
if mibBuilder.loadTexts:
    clCSCMXConfigGroup.setStatus("deprecated")

clCSDxConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 2, 2, 5)
)
clCSDxConfigGroup.setObjects(
    ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSDxMode")
)
if mibBuilder.loadTexts:
    clCSDxConfigGroup.setStatus("current")

clCSNATrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 2, 2, 6)
)
clCSNATrapGroup.setObjects(
      *(("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorLradMacAddr"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorStatus"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorErrCode"))
)
if mibBuilder.loadTexts:
    clCSNATrapGroup.setStatus("current")

clCSSecTunConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 2, 2, 8)
)
clCSSecTunConfigGroup.setObjects(
      *(("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunEnable"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunTlsGwFqdn"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunTlsGwIpAddrType"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunTlsGwIpAddr"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunTlsGwPort"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunPskId"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunPskKey"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunRadiusEnable"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunSnmpTrapEnable"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "cLSCSecTunNetworkRowStatus"))
)
if mibBuilder.loadTexts:
    clCSSecTunConfigGroup.setStatus("current")

clCSSecTunInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 2, 2, 9)
)
clCSSecTunInfoGroup.setObjects(
      *(("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunCurrentState"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunTlsGwIpAddrInUseType"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunTlsGwIpInUseAddr"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunInnerIpAddrType"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunInnerIpAddr"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunTLSClientProcState"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "cLSCSecTunRouteTableRowStatus"))
)
if mibBuilder.loadTexts:
    clCSSecTunInfoGroup.setStatus("current")

clCSNAGlobalConfigGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 2, 2, 11)
)
clCSNAGlobalConfigGroupRev1.setObjects(
      *(("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNAEnable"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorBackhaulSSID"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorBackhaulAuthType"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorBackhaulEapType"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorBackhaulUsername"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorBackhaulPassword"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorBackhaulPsk"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorBackhaulPskMode"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNAServerOnchangeEnable"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNAServerSyncInterval"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNAServerSubscriptionAction"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNAServerSubscriptionTopic"))
)
if mibBuilder.loadTexts:
    clCSNAGlobalConfigGroupRev1.setStatus("deprecated")

clCSNAGlobalConfigGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 2, 2, 12)
)
clCSNAGlobalConfigGroupRev2.setObjects(
      *(("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNAEnable"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorBackhaulSSID"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorBackhaulAuthType"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorBackhaulEapType"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorBackhaulUsername"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorBackhaulPassword"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorBackhaulPsk"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorBackhaulPskMode"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNAServerChannelSyncInterval"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNAServerChannelOnChangeMode"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNAServerChannelRowStatus"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNAServerIsFilterChannel"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "cLCSNAServerResetSubscriptions"))
)
if mibBuilder.loadTexts:
    clCSNAGlobalConfigGroupRev2.setStatus("current")

clCSWebhookConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 2, 2, 13)
)
clCSWebhookConfigGroup.setObjects(
      *(("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSWebhookUrl"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSWebhookAuthToken"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSWebhookEnable"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSWebhookOnchangeEnable"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSWebhookSyncInterval"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSWebhookSubscriptionAction"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSWebhookSubscriptionTopic"))
)
if mibBuilder.loadTexts:
    clCSWebhookConfigGroup.setStatus("deprecated")

clCSWebhookConfigGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 2, 2, 14)
)
clCSWebhookConfigGroupRev1.setObjects(
      *(("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSWebhookUrl"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSWebhookAuthToken"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSWebhookEnable"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSWebhookChannelSyncInterval"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSWebhookChannelOnChangeMode"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSWebhookChannelRowStatus"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "cLCSWebhookResetSubscriptions"))
)
if mibBuilder.loadTexts:
    clCSWebhookConfigGroupRev1.setStatus("current")

clCSCMXConfigGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 2, 2, 15)
)
clCSCMXConfigGroupRev1.setObjects(
      *(("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSCMXEnable"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSCMXOnPremisesEnable"))
)
if mibBuilder.loadTexts:
    clCSCMXConfigGroupRev1.setStatus("current")

clCSTelemetryConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 2, 2, 16)
)
clCSTelemetryConfigGroup.setObjects(
      *(("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSTelemetryFCParent"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSTelemetryFCSubStatus"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSTelemetryFCFilterCount"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSTelemetryFCRowStatus"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSTelemetryFCFilterRowStatus"))
)
if mibBuilder.loadTexts:
    clCSTelemetryConfigGroup.setStatus("current")


# Notification objects

clCSNASensorNotReachableDevStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 0, 0, 1)
)
clCSNASensorNotReachableDevStatus.setObjects(
      *(("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorLradMacAddr"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorStatus"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorErrCode"))
)
if mibBuilder.loadTexts:
    clCSNASensorNotReachableDevStatus.setStatus(
        "current"
    )

clCSSecTunStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 0, 1, 1)
)
clCSSecTunStateChange.setObjects(
    ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunCurrentState")
)
if mibBuilder.loadTexts:
    clCSSecTunStateChange.setStatus(
        "current"
    )


# Notifications groups

clCSNASensorTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 2, 2, 7)
)
clCSNASensorTrapGroup.setObjects(
    ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorNotReachableDevStatus")
)
if mibBuilder.loadTexts:
    clCSNASensorTrapGroup.setStatus(
        "current"
    )

clCSSecTunNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 2, 2, 10)
)
clCSSecTunNotifsGroup.setObjects(
    ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunStateChange")
)
if mibBuilder.loadTexts:
    clCSSecTunNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

clCSMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 2, 1, 1)
)
clCSMIBCompliance.setObjects(
      *(("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNAServerConfigGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNAGlobalConfigGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSCMXServerConfigGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSCMXConfigGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNATrapGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorTrapGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSDxConfigGroup"))
)
if mibBuilder.loadTexts:
    clCSMIBCompliance.setStatus(
        "deprecated"
    )

clCSMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 2, 1, 2)
)
clCSMIBComplianceRev1.setObjects(
      *(("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNAServerConfigGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNAGlobalConfigGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSCMXServerConfigGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSCMXConfigGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNATrapGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorTrapGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSDxConfigGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunConfigGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunInfoGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunNotifsGroup"))
)
if mibBuilder.loadTexts:
    clCSMIBComplianceRev1.setStatus(
        "deprecated"
    )

clCSMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 2, 1, 3)
)
clCSMIBComplianceRev2.setObjects(
      *(("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNAServerConfigGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNAGlobalConfigGroupRev1"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSCMXServerConfigGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSCMXConfigGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNATrapGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorTrapGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSDxConfigGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunConfigGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunInfoGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunNotifsGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSWebhookConfigGroup"))
)
if mibBuilder.loadTexts:
    clCSMIBComplianceRev2.setStatus(
        "deprecated"
    )

clCSMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 838, 2, 1, 4)
)
clCSMIBComplianceRev3.setObjects(
      *(("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNAServerConfigGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNAGlobalConfigGroupRev2"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSCMXServerConfigGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSCMXConfigGroupRev1"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNATrapGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSNASensorTrapGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSDxConfigGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunConfigGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunInfoGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSSecTunNotifsGroup"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSWebhookConfigGroupRev1"),
        ("CISCO-LWAPP-CLOUD-SERVICES-MIB", "clCSTelemetryConfigGroup"))
)
if mibBuilder.loadTexts:
    clCSMIBComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-CLOUD-SERVICES-MIB",
    **{"ciscoLwappCloudServicesMIB": ciscoLwappCloudServicesMIB,
       "clCSMIBNotifs": clCSMIBNotifs,
       "clCSNANotifs": clCSNANotifs,
       "clCSNASensorNotReachableDevStatus": clCSNASensorNotReachableDevStatus,
       "clCSSecTunNotifs": clCSSecTunNotifs,
       "clCSSecTunStateChange": clCSSecTunStateChange,
       "clCSMIBObjects": clCSMIBObjects,
       "clCSNAObjects": clCSNAObjects,
       "clCSNAServerConfig": clCSNAServerConfig,
       "clCSNAServerUrl": clCSNAServerUrl,
       "clCSNAServerIdToken": clCSNAServerIdToken,
       "clCSNAServerOnchangeEnable": clCSNAServerOnchangeEnable,
       "clCSNAServerSyncInterval": clCSNAServerSyncInterval,
       "clCSNAServerSubscriptionAction": clCSNAServerSubscriptionAction,
       "clCSNAServerSubscriptionTopic": clCSNAServerSubscriptionTopic,
       "cLCSNAServerResetSubscriptions": cLCSNAServerResetSubscriptions,
       "clCSNAGlobalConfig": clCSNAGlobalConfig,
       "clCSNAEnable": clCSNAEnable,
       "clCSNASensorBackhaulSSID": clCSNASensorBackhaulSSID,
       "clCSNASensorBackhaulAuthType": clCSNASensorBackhaulAuthType,
       "clCSNASensorBackhaulEapType": clCSNASensorBackhaulEapType,
       "clCSNASensorBackhaulUsername": clCSNASensorBackhaulUsername,
       "clCSNASensorBackhaulPassword": clCSNASensorBackhaulPassword,
       "clCSNASensorBackhaulPskMode": clCSNASensorBackhaulPskMode,
       "clCSNASensorBackhaulPsk": clCSNASensorBackhaulPsk,
       "clCSNAASIEnable": clCSNAASIEnable,
       "clCSNADiffSyncEnable": clCSNADiffSyncEnable,
       "clCSNATrapMgmtObjects": clCSNATrapMgmtObjects,
       "clCSNASensorLradMacAddr": clCSNASensorLradMacAddr,
       "clCSNASensorStatus": clCSNASensorStatus,
       "clCSNASensorErrCode": clCSNASensorErrCode,
       "clCSNAServerConfigTable": clCSNAServerConfigTable,
       "cLCSNAServerChannelTable": cLCSNAServerChannelTable,
       "cLCSNAServerChannelEntry": cLCSNAServerChannelEntry,
       "clCSNAServerChannelName": clCSNAServerChannelName,
       "clCSNAServerChannelSyncInterval": clCSNAServerChannelSyncInterval,
       "clCSNAServerChannelOnChangeMode": clCSNAServerChannelOnChangeMode,
       "clCSNAServerIsFilterChannel": clCSNAServerIsFilterChannel,
       "clCSNAServerChannelRowStatus": clCSNAServerChannelRowStatus,
       "clCSDXObjects": clCSDXObjects,
       "clCSDxConfig": clCSDxConfig,
       "clCSDxMode": clCSDxMode,
       "clCSCMXObjects": clCSCMXObjects,
       "clCSCMXServerConfig": clCSCMXServerConfig,
       "clCSCMXServerUrl": clCSCMXServerUrl,
       "clCSCMXServerIdToken": clCSCMXServerIdToken,
       "clCSCMXConfig": clCSCMXConfig,
       "clCSCMXEnable": clCSCMXEnable,
       "clCSCMXOnPremisesEnable": clCSCMXOnPremisesEnable,
       "clCSSecTunObjects": clCSSecTunObjects,
       "clCSSecTunConfig": clCSSecTunConfig,
       "clCSSecTunEnable": clCSSecTunEnable,
       "clCSSecTunTlsGwFqdn": clCSSecTunTlsGwFqdn,
       "clCSSecTunTlsGwIpAddrType": clCSSecTunTlsGwIpAddrType,
       "clCSSecTunTlsGwIpAddr": clCSSecTunTlsGwIpAddr,
       "clCSSecTunTlsGwPort": clCSSecTunTlsGwPort,
       "clCSSecTunPskId": clCSSecTunPskId,
       "clCSSecTunPskKey": clCSSecTunPskKey,
       "clCSSecTunRadiusEnable": clCSSecTunRadiusEnable,
       "clCSSecTunSnmpTrapEnable": clCSSecTunSnmpTrapEnable,
       "cLCSSecTunStaticNetworkTable": cLCSSecTunStaticNetworkTable,
       "cLCSSecTunStaticNetworkEntry": cLCSSecTunStaticNetworkEntry,
       "cLSCSecTunNetworkIPAddressType": cLSCSecTunNetworkIPAddressType,
       "cLSCSecTunNetworkIPAddress": cLSCSecTunNetworkIPAddress,
       "cLSCSecTunNetworkIPNetmaskType": cLSCSecTunNetworkIPNetmaskType,
       "cLSCSecTunNetworkIPNetmask": cLSCSecTunNetworkIPNetmask,
       "cLSCSecTunNetworkRowStatus": cLSCSecTunNetworkRowStatus,
       "clCSSecTunInfo": clCSSecTunInfo,
       "clCSSecTunCurrentState": clCSSecTunCurrentState,
       "clCSSecTunTlsGwIpAddrInUseType": clCSSecTunTlsGwIpAddrInUseType,
       "clCSSecTunTlsGwIpInUseAddr": clCSSecTunTlsGwIpInUseAddr,
       "clCSSecTunInnerIpAddrType": clCSSecTunInnerIpAddrType,
       "clCSSecTunInnerIpAddr": clCSSecTunInnerIpAddr,
       "clCSSecTunTLSClientProcState": clCSSecTunTLSClientProcState,
       "cLCSSecTunRouteTable": cLCSSecTunRouteTable,
       "cLCSSecTunRouteEntry": cLCSSecTunRouteEntry,
       "cLSCSecTunRouteIPAddressType": cLSCSecTunRouteIPAddressType,
       "cLSCSecTunRouteIPAddress": cLSCSecTunRouteIPAddress,
       "cLSCSecTunRouteNetmaskType": cLSCSecTunRouteNetmaskType,
       "cLSCSecTunRouteNetmask": cLSCSecTunRouteNetmask,
       "cLSCSecTunRouteTableRowStatus": cLSCSecTunRouteTableRowStatus,
       "clCSWebhookGlobalObjects": clCSWebhookGlobalObjects,
       "clCSWebhookUrl": clCSWebhookUrl,
       "clCSWebhookAuthToken": clCSWebhookAuthToken,
       "clCSWebhookEnable": clCSWebhookEnable,
       "clCSWebhookOnchangeEnable": clCSWebhookOnchangeEnable,
       "clCSWebhookSyncInterval": clCSWebhookSyncInterval,
       "clCSWebhookSubscriptionAction": clCSWebhookSubscriptionAction,
       "clCSWebhookSubscriptionTopic": clCSWebhookSubscriptionTopic,
       "cLCSWebhookResetSubscriptions": cLCSWebhookResetSubscriptions,
       "clCSWebhookTableObjects": clCSWebhookTableObjects,
       "cLCSWebhookChannelTable": cLCSWebhookChannelTable,
       "cLCSWebhookChannelEntry": cLCSWebhookChannelEntry,
       "clCSWebhookChannelName": clCSWebhookChannelName,
       "clCSWebhookChannelSyncInterval": clCSWebhookChannelSyncInterval,
       "clCSWebhookChannelOnChangeMode": clCSWebhookChannelOnChangeMode,
       "clCSWebhookChannelRowStatus": clCSWebhookChannelRowStatus,
       "clCSFilterChanTableObjects": clCSFilterChanTableObjects,
       "cLCSTelemetryFCTable": cLCSTelemetryFCTable,
       "cLCSTelemetryFCEntry": cLCSTelemetryFCEntry,
       "clCSTelemetryFCName": clCSTelemetryFCName,
       "clCSTelemetryFCParent": clCSTelemetryFCParent,
       "clCSTelemetryFCSubStatus": clCSTelemetryFCSubStatus,
       "clCSTelemetryFCFilterCount": clCSTelemetryFCFilterCount,
       "clCSTelemetryFCRowStatus": clCSTelemetryFCRowStatus,
       "cLCSTelemetryFCFilterTable": cLCSTelemetryFCFilterTable,
       "cLCSTelemetryFCFilterEntry": cLCSTelemetryFCFilterEntry,
       "clCSTelemetryFCFilter": clCSTelemetryFCFilter,
       "clCSTelemetryFCFilterRowStatus": clCSTelemetryFCFilterRowStatus,
       "clCSMIBConform": clCSMIBConform,
       "clCSMIBCompliances": clCSMIBCompliances,
       "clCSMIBCompliance": clCSMIBCompliance,
       "clCSMIBComplianceRev1": clCSMIBComplianceRev1,
       "clCSMIBComplianceRev2": clCSMIBComplianceRev2,
       "clCSMIBComplianceRev3": clCSMIBComplianceRev3,
       "clCSMIBGroups": clCSMIBGroups,
       "clCSNAServerConfigGroup": clCSNAServerConfigGroup,
       "clCSNAGlobalConfigGroup": clCSNAGlobalConfigGroup,
       "clCSCMXServerConfigGroup": clCSCMXServerConfigGroup,
       "clCSCMXConfigGroup": clCSCMXConfigGroup,
       "clCSDxConfigGroup": clCSDxConfigGroup,
       "clCSNATrapGroup": clCSNATrapGroup,
       "clCSNASensorTrapGroup": clCSNASensorTrapGroup,
       "clCSSecTunConfigGroup": clCSSecTunConfigGroup,
       "clCSSecTunInfoGroup": clCSSecTunInfoGroup,
       "clCSSecTunNotifsGroup": clCSSecTunNotifsGroup,
       "clCSNAGlobalConfigGroupRev1": clCSNAGlobalConfigGroupRev1,
       "clCSNAGlobalConfigGroupRev2": clCSNAGlobalConfigGroupRev2,
       "clCSWebhookConfigGroup": clCSWebhookConfigGroup,
       "clCSWebhookConfigGroupRev1": clCSWebhookConfigGroupRev1,
       "clCSCMXConfigGroupRev1": clCSCMXConfigGroupRev1,
       "clCSTelemetryConfigGroup": clCSTelemetryConfigGroup}
)
