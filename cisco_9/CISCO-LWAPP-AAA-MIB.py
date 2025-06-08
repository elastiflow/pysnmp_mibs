# SNMP MIB module (CISCO-LWAPP-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-AAA-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:47:34 2025
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

(CLSecKeyFormat,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-TC-MIB",
    "CLSecKeyFormat")

(cLWlanIndex,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLWlanIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoURLString,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoURLString")

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
 StorageType,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappAAAMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 598)
)
if mibBuilder.loadTexts:
    ciscoLwappAAAMIB.setRevisions(
        ("2017-03-17 00:00",
         "2010-07-25 00:00",
         "2006-11-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappAAAMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappAAAMIBNotifs = _CiscoLwappAAAMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 0)
)
_CiscoLwappAAAMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappAAAMIBObjects = _CiscoLwappAAAMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1)
)
_ClaConfigObjects_ObjectIdentity = ObjectIdentity
claConfigObjects = _ClaConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1)
)
_ClaPriorityTable_Object = MibTable
claPriorityTable = _ClaPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 1)
)
if mibBuilder.loadTexts:
    claPriorityTable.setStatus("current")
_ClaPriorityEntry_Object = MibTableRow
claPriorityEntry = _ClaPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 1, 1)
)
claPriorityEntry.setIndexNames(
    (0, "CISCO-LWAPP-AAA-MIB", "claPriorityAuth"),
)
if mibBuilder.loadTexts:
    claPriorityEntry.setStatus("current")


class _ClaPriorityAuth_Type(Integer32):
    """Custom type claPriorityAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("radius", 2),
          ("tacacsplus", 3))
    )


_ClaPriorityAuth_Type.__name__ = "Integer32"
_ClaPriorityAuth_Object = MibTableColumn
claPriorityAuth = _ClaPriorityAuth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 1, 1, 1),
    _ClaPriorityAuth_Type()
)
claPriorityAuth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    claPriorityAuth.setStatus("current")


class _ClaPriorityOrder_Type(Unsigned32):
    """Custom type claPriorityOrder based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_ClaPriorityOrder_Type.__name__ = "Unsigned32"
_ClaPriorityOrder_Object = MibTableColumn
claPriorityOrder = _ClaPriorityOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 1, 1, 2),
    _ClaPriorityOrder_Type()
)
claPriorityOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claPriorityOrder.setStatus("current")
_ClaTacacsServerTable_Object = MibTable
claTacacsServerTable = _ClaTacacsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2)
)
if mibBuilder.loadTexts:
    claTacacsServerTable.setStatus("current")
_ClaTacacsServerEntry_Object = MibTableRow
claTacacsServerEntry = _ClaTacacsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1)
)
claTacacsServerEntry.setIndexNames(
    (0, "CISCO-LWAPP-AAA-MIB", "claTacacsServerType"),
    (0, "CISCO-LWAPP-AAA-MIB", "claTacacsServerPriority"),
)
if mibBuilder.loadTexts:
    claTacacsServerEntry.setStatus("current")


class _ClaTacacsServerType_Type(Integer32):
    """Custom type claTacacsServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authentication", 1),
          ("authorization", 2),
          ("accounting", 3))
    )


_ClaTacacsServerType_Type.__name__ = "Integer32"
_ClaTacacsServerType_Object = MibTableColumn
claTacacsServerType = _ClaTacacsServerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 1),
    _ClaTacacsServerType_Type()
)
claTacacsServerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    claTacacsServerType.setStatus("current")
_ClaTacacsServerPriority_Type = Unsigned32
_ClaTacacsServerPriority_Object = MibTableColumn
claTacacsServerPriority = _ClaTacacsServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 2),
    _ClaTacacsServerPriority_Type()
)
claTacacsServerPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    claTacacsServerPriority.setStatus("current")
_ClaTacacsServerAddressType_Type = InetAddressType
_ClaTacacsServerAddressType_Object = MibTableColumn
claTacacsServerAddressType = _ClaTacacsServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 3),
    _ClaTacacsServerAddressType_Type()
)
claTacacsServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claTacacsServerAddressType.setStatus("current")
_ClaTacacsServerAddress_Type = InetAddress
_ClaTacacsServerAddress_Object = MibTableColumn
claTacacsServerAddress = _ClaTacacsServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 4),
    _ClaTacacsServerAddress_Type()
)
claTacacsServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claTacacsServerAddress.setStatus("current")
_ClaTacacsServerPortNum_Type = InetPortNumber
_ClaTacacsServerPortNum_Object = MibTableColumn
claTacacsServerPortNum = _ClaTacacsServerPortNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 5),
    _ClaTacacsServerPortNum_Type()
)
claTacacsServerPortNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claTacacsServerPortNum.setStatus("current")


class _ClaTacacsServerEnabled_Type(TruthValue):
    """Custom type claTacacsServerEnabled based on TruthValue"""
    defaultValue = 1


_ClaTacacsServerEnabled_Type.__name__ = "TruthValue"
_ClaTacacsServerEnabled_Object = MibTableColumn
claTacacsServerEnabled = _ClaTacacsServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 6),
    _ClaTacacsServerEnabled_Type()
)
claTacacsServerEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claTacacsServerEnabled.setStatus("current")
_ClaTacacsServerSecretType_Type = CLSecKeyFormat
_ClaTacacsServerSecretType_Object = MibTableColumn
claTacacsServerSecretType = _ClaTacacsServerSecretType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 7),
    _ClaTacacsServerSecretType_Type()
)
claTacacsServerSecretType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claTacacsServerSecretType.setStatus("current")
_ClaTacacsServerSecret_Type = DisplayString
_ClaTacacsServerSecret_Object = MibTableColumn
claTacacsServerSecret = _ClaTacacsServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 8),
    _ClaTacacsServerSecret_Type()
)
claTacacsServerSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claTacacsServerSecret.setStatus("current")


class _ClaTacacsServerTimeout_Type(Unsigned32):
    """Custom type claTacacsServerTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_ClaTacacsServerTimeout_Type.__name__ = "Unsigned32"
_ClaTacacsServerTimeout_Object = MibTableColumn
claTacacsServerTimeout = _ClaTacacsServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 9),
    _ClaTacacsServerTimeout_Type()
)
claTacacsServerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claTacacsServerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    claTacacsServerTimeout.setUnits("seconds")


class _ClaTacacsServerStorageType_Type(StorageType):
    """Custom type claTacacsServerStorageType based on StorageType"""
    defaultValue = 3


_ClaTacacsServerStorageType_Type.__name__ = "StorageType"
_ClaTacacsServerStorageType_Object = MibTableColumn
claTacacsServerStorageType = _ClaTacacsServerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 10),
    _ClaTacacsServerStorageType_Type()
)
claTacacsServerStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claTacacsServerStorageType.setStatus("current")
_ClaTacacsServerRowStatus_Type = RowStatus
_ClaTacacsServerRowStatus_Object = MibTableColumn
claTacacsServerRowStatus = _ClaTacacsServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 2, 1, 11),
    _ClaTacacsServerRowStatus_Type()
)
claTacacsServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claTacacsServerRowStatus.setStatus("current")
_ClaWlanTable_Object = MibTable
claWlanTable = _ClaWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 3)
)
if mibBuilder.loadTexts:
    claWlanTable.setStatus("current")
_ClaWlanEntry_Object = MibTableRow
claWlanEntry = _ClaWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 3, 1)
)
claWlanEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    claWlanEntry.setStatus("current")


class _ClaWlanAcctServerEnabled_Type(TruthValue):
    """Custom type claWlanAcctServerEnabled based on TruthValue"""
    defaultValue = 1


_ClaWlanAcctServerEnabled_Type.__name__ = "TruthValue"
_ClaWlanAcctServerEnabled_Object = MibTableColumn
claWlanAcctServerEnabled = _ClaWlanAcctServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 3, 1, 1),
    _ClaWlanAcctServerEnabled_Type()
)
claWlanAcctServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claWlanAcctServerEnabled.setStatus("current")


class _ClaWlanAuthServerEnabled_Type(TruthValue):
    """Custom type claWlanAuthServerEnabled based on TruthValue"""
    defaultValue = 1


_ClaWlanAuthServerEnabled_Type.__name__ = "TruthValue"
_ClaWlanAuthServerEnabled_Object = MibTableColumn
claWlanAuthServerEnabled = _ClaWlanAuthServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 3, 1, 2),
    _ClaWlanAuthServerEnabled_Type()
)
claWlanAuthServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claWlanAuthServerEnabled.setStatus("current")


class _ClaWlanOverwriteInterface_Type(TruthValue):
    """Custom type claWlanOverwriteInterface based on TruthValue"""
    defaultValue = 2


_ClaWlanOverwriteInterface_Type.__name__ = "TruthValue"
_ClaWlanOverwriteInterface_Object = MibTableColumn
claWlanOverwriteInterface = _ClaWlanOverwriteInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 3, 1, 3),
    _ClaWlanOverwriteInterface_Type()
)
claWlanOverwriteInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claWlanOverwriteInterface.setStatus("current")


class _ClaWlanInterimUpdate_Type(TruthValue):
    """Custom type claWlanInterimUpdate based on TruthValue"""
    defaultValue = 2


_ClaWlanInterimUpdate_Type.__name__ = "TruthValue"
_ClaWlanInterimUpdate_Object = MibTableColumn
claWlanInterimUpdate = _ClaWlanInterimUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 3, 1, 4),
    _ClaWlanInterimUpdate_Type()
)
claWlanInterimUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claWlanInterimUpdate.setStatus("current")


class _ClaWlanInterimUpdateInterval_Type(TimeInterval):
    """Custom type claWlanInterimUpdateInterval based on TimeInterval"""
    defaultValue = 600

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 3600),
    )


_ClaWlanInterimUpdateInterval_Type.__name__ = "TimeInterval"
_ClaWlanInterimUpdateInterval_Object = MibTableColumn
claWlanInterimUpdateInterval = _ClaWlanInterimUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 3, 1, 5),
    _ClaWlanInterimUpdateInterval_Type()
)
claWlanInterimUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claWlanInterimUpdateInterval.setStatus("current")
if mibBuilder.loadTexts:
    claWlanInterimUpdateInterval.setUnits("seconds")


class _ClaRadiusServerGlobalActivatedEnabled_Type(TruthValue):
    """Custom type claRadiusServerGlobalActivatedEnabled based on TruthValue"""
    defaultValue = 1


_ClaRadiusServerGlobalActivatedEnabled_Type.__name__ = "TruthValue"
_ClaRadiusServerGlobalActivatedEnabled_Object = MibScalar
claRadiusServerGlobalActivatedEnabled = _ClaRadiusServerGlobalActivatedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 4),
    _ClaRadiusServerGlobalActivatedEnabled_Type()
)
claRadiusServerGlobalActivatedEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusServerGlobalActivatedEnabled.setStatus("current")


class _ClaRadiusServerGlobalDeactivatedEnabled_Type(TruthValue):
    """Custom type claRadiusServerGlobalDeactivatedEnabled based on TruthValue"""
    defaultValue = 1


_ClaRadiusServerGlobalDeactivatedEnabled_Type.__name__ = "TruthValue"
_ClaRadiusServerGlobalDeactivatedEnabled_Object = MibScalar
claRadiusServerGlobalDeactivatedEnabled = _ClaRadiusServerGlobalDeactivatedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 5),
    _ClaRadiusServerGlobalDeactivatedEnabled_Type()
)
claRadiusServerGlobalDeactivatedEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusServerGlobalDeactivatedEnabled.setStatus("current")


class _ClaRadiusServerWlanActivatedEnabled_Type(TruthValue):
    """Custom type claRadiusServerWlanActivatedEnabled based on TruthValue"""
    defaultValue = 1


_ClaRadiusServerWlanActivatedEnabled_Type.__name__ = "TruthValue"
_ClaRadiusServerWlanActivatedEnabled_Object = MibScalar
claRadiusServerWlanActivatedEnabled = _ClaRadiusServerWlanActivatedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 6),
    _ClaRadiusServerWlanActivatedEnabled_Type()
)
claRadiusServerWlanActivatedEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusServerWlanActivatedEnabled.setStatus("current")


class _ClaRadiusServerWlanDeactivatedEnabled_Type(TruthValue):
    """Custom type claRadiusServerWlanDeactivatedEnabled based on TruthValue"""
    defaultValue = 1


_ClaRadiusServerWlanDeactivatedEnabled_Type.__name__ = "TruthValue"
_ClaRadiusServerWlanDeactivatedEnabled_Object = MibScalar
claRadiusServerWlanDeactivatedEnabled = _ClaRadiusServerWlanDeactivatedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 7),
    _ClaRadiusServerWlanDeactivatedEnabled_Type()
)
claRadiusServerWlanDeactivatedEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusServerWlanDeactivatedEnabled.setStatus("current")


class _ClaRadiusReqTimedOutEnabled_Type(TruthValue):
    """Custom type claRadiusReqTimedOutEnabled based on TruthValue"""
    defaultValue = 1


_ClaRadiusReqTimedOutEnabled_Type.__name__ = "TruthValue"
_ClaRadiusReqTimedOutEnabled_Object = MibScalar
claRadiusReqTimedOutEnabled = _ClaRadiusReqTimedOutEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 8),
    _ClaRadiusReqTimedOutEnabled_Type()
)
claRadiusReqTimedOutEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusReqTimedOutEnabled.setStatus("current")


class _ClaSaveUserData_Type(TruthValue):
    """Custom type claSaveUserData based on TruthValue"""
    defaultValue = 1


_ClaSaveUserData_Type.__name__ = "TruthValue"
_ClaSaveUserData_Object = MibScalar
claSaveUserData = _ClaSaveUserData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 9),
    _ClaSaveUserData_Type()
)
claSaveUserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claSaveUserData.setStatus("current")


class _ClaWebRadiusAuthentication_Type(Integer32):
    """Custom type claWebRadiusAuthentication based on Integer32"""
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
        *(("pap", 1),
          ("chap", 2),
          ("md5-chap", 3))
    )


_ClaWebRadiusAuthentication_Type.__name__ = "Integer32"
_ClaWebRadiusAuthentication_Object = MibScalar
claWebRadiusAuthentication = _ClaWebRadiusAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 10),
    _ClaWebRadiusAuthentication_Type()
)
claWebRadiusAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claWebRadiusAuthentication.setStatus("current")


class _ClaRadiusFallbackMode_Type(Integer32):
    """Custom type claRadiusFallbackMode based on Integer32"""
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
        *(("off", 1),
          ("passive", 2),
          ("active", 3))
    )


_ClaRadiusFallbackMode_Type.__name__ = "Integer32"
_ClaRadiusFallbackMode_Object = MibScalar
claRadiusFallbackMode = _ClaRadiusFallbackMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 11),
    _ClaRadiusFallbackMode_Type()
)
claRadiusFallbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusFallbackMode.setStatus("current")
_ClaRadiusFallbackUsername_Type = SnmpAdminString
_ClaRadiusFallbackUsername_Object = MibScalar
claRadiusFallbackUsername = _ClaRadiusFallbackUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 12),
    _ClaRadiusFallbackUsername_Type()
)
claRadiusFallbackUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusFallbackUsername.setStatus("current")


class _ClaRadiusFallbackInterval_Type(TimeInterval):
    """Custom type claRadiusFallbackInterval based on TimeInterval"""
    defaultValue = 300

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 3600),
    )


_ClaRadiusFallbackInterval_Type.__name__ = "TimeInterval"
_ClaRadiusFallbackInterval_Object = MibScalar
claRadiusFallbackInterval = _ClaRadiusFallbackInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 13),
    _ClaRadiusFallbackInterval_Type()
)
claRadiusFallbackInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusFallbackInterval.setStatus("current")
if mibBuilder.loadTexts:
    claRadiusFallbackInterval.setUnits("seconds")


class _ClaRadiusAuthMacDelimiter_Type(Integer32):
    """Custom type claRadiusAuthMacDelimiter based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noDelimiter", 0),
          ("colon", 1),
          ("hyphen", 2),
          ("singleHyphen", 3))
    )


_ClaRadiusAuthMacDelimiter_Type.__name__ = "Integer32"
_ClaRadiusAuthMacDelimiter_Object = MibScalar
claRadiusAuthMacDelimiter = _ClaRadiusAuthMacDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 14),
    _ClaRadiusAuthMacDelimiter_Type()
)
claRadiusAuthMacDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusAuthMacDelimiter.setStatus("current")


class _ClaRadiusAcctMacDelimiter_Type(Integer32):
    """Custom type claRadiusAcctMacDelimiter based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noDelimiter", 0),
          ("colon", 1),
          ("hyphen", 2),
          ("singleHyphen", 3))
    )


_ClaRadiusAcctMacDelimiter_Type.__name__ = "Integer32"
_ClaRadiusAcctMacDelimiter_Object = MibScalar
claRadiusAcctMacDelimiter = _ClaRadiusAcctMacDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 15),
    _ClaRadiusAcctMacDelimiter_Type()
)
claRadiusAcctMacDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusAcctMacDelimiter.setStatus("current")


class _ClaAcceptMICertificate_Type(TruthValue):
    """Custom type claAcceptMICertificate based on TruthValue"""
    defaultValue = 2


_ClaAcceptMICertificate_Type.__name__ = "TruthValue"
_ClaAcceptMICertificate_Object = MibScalar
claAcceptMICertificate = _ClaAcceptMICertificate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 16),
    _ClaAcceptMICertificate_Type()
)
claAcceptMICertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claAcceptMICertificate.setStatus("current")


class _ClaAcceptLSCertificate_Type(TruthValue):
    """Custom type claAcceptLSCertificate based on TruthValue"""
    defaultValue = 2


_ClaAcceptLSCertificate_Type.__name__ = "TruthValue"
_ClaAcceptLSCertificate_Object = MibScalar
claAcceptLSCertificate = _ClaAcceptLSCertificate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 17),
    _ClaAcceptLSCertificate_Type()
)
claAcceptLSCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claAcceptLSCertificate.setStatus("current")


class _ClaAllowAuthorizeLscApAgainstAAA_Type(TruthValue):
    """Custom type claAllowAuthorizeLscApAgainstAAA based on TruthValue"""
    defaultValue = 2


_ClaAllowAuthorizeLscApAgainstAAA_Type.__name__ = "TruthValue"
_ClaAllowAuthorizeLscApAgainstAAA_Object = MibScalar
claAllowAuthorizeLscApAgainstAAA = _ClaAllowAuthorizeLscApAgainstAAA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 18),
    _ClaAllowAuthorizeLscApAgainstAAA_Type()
)
claAllowAuthorizeLscApAgainstAAA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claAllowAuthorizeLscApAgainstAAA.setStatus("current")


class _ClaSscHashValidationEnabled_Type(TruthValue):
    """Custom type claSscHashValidationEnabled based on TruthValue"""
    defaultValue = 2


_ClaSscHashValidationEnabled_Type.__name__ = "TruthValue"
_ClaSscHashValidationEnabled_Object = MibScalar
claSscHashValidationEnabled = _ClaSscHashValidationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 19),
    _ClaSscHashValidationEnabled_Type()
)
claSscHashValidationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claSscHashValidationEnabled.setStatus("current")


class _ClaSscCertificateSubject_Type(DisplayString):
    """Custom type claSscCertificateSubject based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_ClaSscCertificateSubject_Type.__name__ = "DisplayString"
_ClaSscCertificateSubject_Object = MibScalar
claSscCertificateSubject = _ClaSscCertificateSubject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 20),
    _ClaSscCertificateSubject_Type()
)
claSscCertificateSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claSscCertificateSubject.setStatus("current")


class _ClaSscCertificateValidity_Type(DisplayString):
    """Custom type claSscCertificateValidity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_ClaSscCertificateValidity_Type.__name__ = "DisplayString"
_ClaSscCertificateValidity_Object = MibScalar
claSscCertificateValidity = _ClaSscCertificateValidity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 21),
    _ClaSscCertificateValidity_Type()
)
claSscCertificateValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claSscCertificateValidity.setStatus("current")


class _ClaSscCertificateHashKey_Type(DisplayString):
    """Custom type claSscCertificateHashKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_ClaSscCertificateHashKey_Type.__name__ = "DisplayString"
_ClaSscCertificateHashKey_Object = MibScalar
claSscCertificateHashKey = _ClaSscCertificateHashKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 22),
    _ClaSscCertificateHashKey_Type()
)
claSscCertificateHashKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claSscCertificateHashKey.setStatus("current")
_ClaRadiusAuthServerTable_Object = MibTable
claRadiusAuthServerTable = _ClaRadiusAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 23)
)
if mibBuilder.loadTexts:
    claRadiusAuthServerTable.setStatus("current")
_ClaRadiusAuthServerEntry_Object = MibTableRow
claRadiusAuthServerEntry = _ClaRadiusAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 23, 1)
)
claRadiusAuthServerEntry.setIndexNames(
    (0, "CISCO-LWAPP-AAA-MIB", "claRadiusAuthServerIndex"),
)
if mibBuilder.loadTexts:
    claRadiusAuthServerEntry.setStatus("current")


class _ClaRadiusAuthServerIndex_Type(Integer32):
    """Custom type claRadiusAuthServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17),
    )


_ClaRadiusAuthServerIndex_Type.__name__ = "Integer32"
_ClaRadiusAuthServerIndex_Object = MibTableColumn
claRadiusAuthServerIndex = _ClaRadiusAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 23, 1, 1),
    _ClaRadiusAuthServerIndex_Type()
)
claRadiusAuthServerIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claRadiusAuthServerIndex.setStatus("current")


class _ClaRadiusAuthServerIPSecAuthMethod_Type(Integer32):
    """Custom type claRadiusAuthServerIPSecAuthMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("psk", 1),
          ("cert", 2))
    )


_ClaRadiusAuthServerIPSecAuthMethod_Type.__name__ = "Integer32"
_ClaRadiusAuthServerIPSecAuthMethod_Object = MibTableColumn
claRadiusAuthServerIPSecAuthMethod = _ClaRadiusAuthServerIPSecAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 23, 1, 2),
    _ClaRadiusAuthServerIPSecAuthMethod_Type()
)
claRadiusAuthServerIPSecAuthMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claRadiusAuthServerIPSecAuthMethod.setStatus("current")


class _ClaRadiusAuthServerKey_Type(OctetString):
    """Custom type claRadiusAuthServerKey based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ClaRadiusAuthServerKey_Type.__name__ = "OctetString"
_ClaRadiusAuthServerKey_Object = MibTableColumn
claRadiusAuthServerKey = _ClaRadiusAuthServerKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 23, 1, 3),
    _ClaRadiusAuthServerKey_Type()
)
claRadiusAuthServerKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claRadiusAuthServerKey.setStatus("current")


class _ClaRadiusAuthServerKeyFormat_Type(Integer32):
    """Custom type claRadiusAuthServerKeyFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hex", 1),
          ("ascii", 2))
    )


_ClaRadiusAuthServerKeyFormat_Type.__name__ = "Integer32"
_ClaRadiusAuthServerKeyFormat_Object = MibTableColumn
claRadiusAuthServerKeyFormat = _ClaRadiusAuthServerKeyFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 23, 1, 4),
    _ClaRadiusAuthServerKeyFormat_Type()
)
claRadiusAuthServerKeyFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claRadiusAuthServerKeyFormat.setStatus("current")


class _ClaRadiusAuthServerIsActive_Type(Integer32):
    """Custom type claRadiusAuthServerIsActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ClaRadiusAuthServerIsActive_Type.__name__ = "Integer32"
_ClaRadiusAuthServerIsActive_Object = MibTableColumn
claRadiusAuthServerIsActive = _ClaRadiusAuthServerIsActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 23, 1, 5),
    _ClaRadiusAuthServerIsActive_Type()
)
claRadiusAuthServerIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claRadiusAuthServerIsActive.setStatus("current")
_ClaRadiusAuthServerTunnelProxy_Type = TruthValue
_ClaRadiusAuthServerTunnelProxy_Object = MibTableColumn
claRadiusAuthServerTunnelProxy = _ClaRadiusAuthServerTunnelProxy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 23, 1, 6),
    _ClaRadiusAuthServerTunnelProxy_Type()
)
claRadiusAuthServerTunnelProxy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claRadiusAuthServerTunnelProxy.setStatus("current")


class _ClaRadiusAuthServerPacState_Type(TruthValue):
    """Custom type claRadiusAuthServerPacState based on TruthValue"""
    defaultValue = 2


_ClaRadiusAuthServerPacState_Type.__name__ = "TruthValue"
_ClaRadiusAuthServerPacState_Object = MibTableColumn
claRadiusAuthServerPacState = _ClaRadiusAuthServerPacState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 23, 1, 7),
    _ClaRadiusAuthServerPacState_Type()
)
claRadiusAuthServerPacState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claRadiusAuthServerPacState.setStatus("current")
_ClaRadiusAccServerTable_Object = MibTable
claRadiusAccServerTable = _ClaRadiusAccServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 24)
)
if mibBuilder.loadTexts:
    claRadiusAccServerTable.setStatus("current")
_ClaRadiusAccServerEntry_Object = MibTableRow
claRadiusAccServerEntry = _ClaRadiusAccServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 24, 1)
)
claRadiusAccServerEntry.setIndexNames(
    (0, "CISCO-LWAPP-AAA-MIB", "claRadiusAccServerIndex"),
)
if mibBuilder.loadTexts:
    claRadiusAccServerEntry.setStatus("current")


class _ClaRadiusAccServerIndex_Type(Integer32):
    """Custom type claRadiusAccServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17),
    )


_ClaRadiusAccServerIndex_Type.__name__ = "Integer32"
_ClaRadiusAccServerIndex_Object = MibTableColumn
claRadiusAccServerIndex = _ClaRadiusAccServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 24, 1, 1),
    _ClaRadiusAccServerIndex_Type()
)
claRadiusAccServerIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claRadiusAccServerIndex.setStatus("current")


class _ClaRadiusAccServerIPSecAuthMethod_Type(Integer32):
    """Custom type claRadiusAccServerIPSecAuthMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("psk", 1),
          ("cert", 2))
    )


_ClaRadiusAccServerIPSecAuthMethod_Type.__name__ = "Integer32"
_ClaRadiusAccServerIPSecAuthMethod_Object = MibTableColumn
claRadiusAccServerIPSecAuthMethod = _ClaRadiusAccServerIPSecAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 24, 1, 2),
    _ClaRadiusAccServerIPSecAuthMethod_Type()
)
claRadiusAccServerIPSecAuthMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claRadiusAccServerIPSecAuthMethod.setStatus("current")


class _ClaRadiusAccServerKey_Type(OctetString):
    """Custom type claRadiusAccServerKey based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ClaRadiusAccServerKey_Type.__name__ = "OctetString"
_ClaRadiusAccServerKey_Object = MibTableColumn
claRadiusAccServerKey = _ClaRadiusAccServerKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 24, 1, 3),
    _ClaRadiusAccServerKey_Type()
)
claRadiusAccServerKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claRadiusAccServerKey.setStatus("current")


class _ClaRadiusAccServerKeyFormat_Type(Integer32):
    """Custom type claRadiusAccServerKeyFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hex", 1),
          ("ascii", 2))
    )


_ClaRadiusAccServerKeyFormat_Type.__name__ = "Integer32"
_ClaRadiusAccServerKeyFormat_Object = MibTableColumn
claRadiusAccServerKeyFormat = _ClaRadiusAccServerKeyFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 24, 1, 4),
    _ClaRadiusAccServerKeyFormat_Type()
)
claRadiusAccServerKeyFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claRadiusAccServerKeyFormat.setStatus("current")


class _ClaRadiusAccServerIsActive_Type(Integer32):
    """Custom type claRadiusAccServerIsActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ClaRadiusAccServerIsActive_Type.__name__ = "Integer32"
_ClaRadiusAccServerIsActive_Object = MibTableColumn
claRadiusAccServerIsActive = _ClaRadiusAccServerIsActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 24, 1, 5),
    _ClaRadiusAccServerIsActive_Type()
)
claRadiusAccServerIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claRadiusAccServerIsActive.setStatus("current")
_ClaRadiusAccServerTunnelProxy_Type = TruthValue
_ClaRadiusAccServerTunnelProxy_Object = MibTableColumn
claRadiusAccServerTunnelProxy = _ClaRadiusAccServerTunnelProxy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 24, 1, 6),
    _ClaRadiusAccServerTunnelProxy_Type()
)
claRadiusAccServerTunnelProxy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claRadiusAccServerTunnelProxy.setStatus("current")


class _ClaRadiusAccServerPacState_Type(TruthValue):
    """Custom type claRadiusAccServerPacState based on TruthValue"""
    defaultValue = 2


_ClaRadiusAccServerPacState_Type.__name__ = "TruthValue"
_ClaRadiusAccServerPacState_Object = MibTableColumn
claRadiusAccServerPacState = _ClaRadiusAccServerPacState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 24, 1, 7),
    _ClaRadiusAccServerPacState_Type()
)
claRadiusAccServerPacState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claRadiusAccServerPacState.setStatus("current")
_ClaRadiusAuthServerRealmTable_Object = MibTable
claRadiusAuthServerRealmTable = _ClaRadiusAuthServerRealmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 25)
)
if mibBuilder.loadTexts:
    claRadiusAuthServerRealmTable.setStatus("current")
_ClaRadiusAuthServerRealmEntry_Object = MibTableRow
claRadiusAuthServerRealmEntry = _ClaRadiusAuthServerRealmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 25, 1)
)
claRadiusAuthServerRealmEntry.setIndexNames(
    (0, "CISCO-LWAPP-AAA-MIB", "claRadiusAuthServerIndex"),
    (0, "CISCO-LWAPP-AAA-MIB", "claRadiusAuthServerRealm"),
)
if mibBuilder.loadTexts:
    claRadiusAuthServerRealmEntry.setStatus("current")
_ClaRadiusAuthServerRealm_Type = SnmpAdminString
_ClaRadiusAuthServerRealm_Object = MibTableColumn
claRadiusAuthServerRealm = _ClaRadiusAuthServerRealm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 25, 1, 1),
    _ClaRadiusAuthServerRealm_Type()
)
claRadiusAuthServerRealm.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    claRadiusAuthServerRealm.setStatus("current")
_ClaRadiusAuthRealmRowStatus_Type = RowStatus
_ClaRadiusAuthRealmRowStatus_Object = MibTableColumn
claRadiusAuthRealmRowStatus = _ClaRadiusAuthRealmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 25, 1, 2),
    _ClaRadiusAuthRealmRowStatus_Type()
)
claRadiusAuthRealmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claRadiusAuthRealmRowStatus.setStatus("current")
_ClaRadiusAcctServerRealmTable_Object = MibTable
claRadiusAcctServerRealmTable = _ClaRadiusAcctServerRealmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 26)
)
if mibBuilder.loadTexts:
    claRadiusAcctServerRealmTable.setStatus("current")
_ClaRadiusAcctServerRealmEntry_Object = MibTableRow
claRadiusAcctServerRealmEntry = _ClaRadiusAcctServerRealmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 26, 1)
)
claRadiusAcctServerRealmEntry.setIndexNames(
    (0, "CISCO-LWAPP-AAA-MIB", "claRadiusAccServerIndex"),
    (0, "CISCO-LWAPP-AAA-MIB", "claRadiusAcctServerRealm"),
)
if mibBuilder.loadTexts:
    claRadiusAcctServerRealmEntry.setStatus("current")
_ClaRadiusAcctServerRealm_Type = SnmpAdminString
_ClaRadiusAcctServerRealm_Object = MibTableColumn
claRadiusAcctServerRealm = _ClaRadiusAcctServerRealm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 26, 1, 1),
    _ClaRadiusAcctServerRealm_Type()
)
claRadiusAcctServerRealm.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    claRadiusAcctServerRealm.setStatus("current")
_ClaRadiusAcctRealmRowStatus_Type = RowStatus
_ClaRadiusAcctRealmRowStatus_Object = MibTableColumn
claRadiusAcctRealmRowStatus = _ClaRadiusAcctRealmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 26, 1, 2),
    _ClaRadiusAcctRealmRowStatus_Type()
)
claRadiusAcctRealmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claRadiusAcctRealmRowStatus.setStatus("current")
_ClaTacacsFallbackTestInterval_Type = Unsigned32
_ClaTacacsFallbackTestInterval_Object = MibScalar
claTacacsFallbackTestInterval = _ClaTacacsFallbackTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 1, 27),
    _ClaTacacsFallbackTestInterval_Type()
)
claTacacsFallbackTestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claTacacsFallbackTestInterval.setStatus("current")
if mibBuilder.loadTexts:
    claTacacsFallbackTestInterval.setUnits("seconds")
_ClaStatusObjects_ObjectIdentity = ObjectIdentity
claStatusObjects = _ClaStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2)
)
_ClaRadiusServerTable_Object = MibTable
claRadiusServerTable = _ClaRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1)
)
if mibBuilder.loadTexts:
    claRadiusServerTable.setStatus("current")
_ClaRadiusServerEntry_Object = MibTableRow
claRadiusServerEntry = _ClaRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1, 1)
)
claRadiusServerEntry.setIndexNames(
    (0, "CISCO-LWAPP-AAA-MIB", "claRadiusReqId"),
)
if mibBuilder.loadTexts:
    claRadiusServerEntry.setStatus("current")
_ClaRadiusReqId_Type = Unsigned32
_ClaRadiusReqId_Object = MibTableColumn
claRadiusReqId = _ClaRadiusReqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1, 1, 1),
    _ClaRadiusReqId_Type()
)
claRadiusReqId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    claRadiusReqId.setStatus("current")
_ClaRadiusAddressType_Type = InetAddressType
_ClaRadiusAddressType_Object = MibTableColumn
claRadiusAddressType = _ClaRadiusAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1, 1, 2),
    _ClaRadiusAddressType_Type()
)
claRadiusAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claRadiusAddressType.setStatus("current")
_ClaRadiusAddress_Type = InetAddress
_ClaRadiusAddress_Object = MibTableColumn
claRadiusAddress = _ClaRadiusAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1, 1, 3),
    _ClaRadiusAddress_Type()
)
claRadiusAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claRadiusAddress.setStatus("current")
_ClaRadiusPortNum_Type = InetPortNumber
_ClaRadiusPortNum_Object = MibTableColumn
claRadiusPortNum = _ClaRadiusPortNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1, 1, 4),
    _ClaRadiusPortNum_Type()
)
claRadiusPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claRadiusPortNum.setStatus("current")


class _ClaRadiusWlanIdx_Type(Unsigned32):
    """Custom type claRadiusWlanIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17),
    )


_ClaRadiusWlanIdx_Type.__name__ = "Unsigned32"
_ClaRadiusWlanIdx_Object = MibTableColumn
claRadiusWlanIdx = _ClaRadiusWlanIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1, 1, 5),
    _ClaRadiusWlanIdx_Type()
)
claRadiusWlanIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claRadiusWlanIdx.setStatus("current")
_ClaRadiusClientMacAddress_Type = MacAddress
_ClaRadiusClientMacAddress_Object = MibTableColumn
claRadiusClientMacAddress = _ClaRadiusClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1, 1, 6),
    _ClaRadiusClientMacAddress_Type()
)
claRadiusClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claRadiusClientMacAddress.setStatus("current")
_ClaRadiusUserName_Type = DisplayString
_ClaRadiusUserName_Object = MibTableColumn
claRadiusUserName = _ClaRadiusUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 1, 1, 7),
    _ClaRadiusUserName_Type()
)
claRadiusUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claRadiusUserName.setStatus("current")
_ClaDBCurrentUsedEntries_Type = Gauge32
_ClaDBCurrentUsedEntries_Object = MibScalar
claDBCurrentUsedEntries = _ClaDBCurrentUsedEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 2),
    _ClaDBCurrentUsedEntries_Type()
)
claDBCurrentUsedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claDBCurrentUsedEntries.setStatus("current")
_ClaRadiusAuthClientAccessRequestsTotal_Type = Counter32
_ClaRadiusAuthClientAccessRequestsTotal_Object = MibScalar
claRadiusAuthClientAccessRequestsTotal = _ClaRadiusAuthClientAccessRequestsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 3),
    _ClaRadiusAuthClientAccessRequestsTotal_Type()
)
claRadiusAuthClientAccessRequestsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claRadiusAuthClientAccessRequestsTotal.setStatus("current")
_ClaRadiusAuthClientAccessResponseTotal_Type = Counter32
_ClaRadiusAuthClientAccessResponseTotal_Object = MibScalar
claRadiusAuthClientAccessResponseTotal = _ClaRadiusAuthClientAccessResponseTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 4),
    _ClaRadiusAuthClientAccessResponseTotal_Type()
)
claRadiusAuthClientAccessResponseTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claRadiusAuthClientAccessResponseTotal.setStatus("current")
_ClaRadiusAuthClientAccessAcceptsTotal_Type = Counter32
_ClaRadiusAuthClientAccessAcceptsTotal_Object = MibScalar
claRadiusAuthClientAccessAcceptsTotal = _ClaRadiusAuthClientAccessAcceptsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 5),
    _ClaRadiusAuthClientAccessAcceptsTotal_Type()
)
claRadiusAuthClientAccessAcceptsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claRadiusAuthClientAccessAcceptsTotal.setStatus("current")
_ClaRadiusServerAvpTable_Object = MibTable
claRadiusServerAvpTable = _ClaRadiusServerAvpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 6)
)
if mibBuilder.loadTexts:
    claRadiusServerAvpTable.setStatus("current")
_ClaRadiusServerAvpEntry_Object = MibTableRow
claRadiusServerAvpEntry = _ClaRadiusServerAvpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 6, 1)
)
claRadiusServerAvpEntry.setIndexNames(
    (0, "CISCO-LWAPP-AAA-MIB", "claWlanId"),
    (0, "CISCO-LWAPP-AAA-MIB", "claRadiusType"),
    (0, "CISCO-LWAPP-AAA-MIB", "claAvpEntryId"),
)
if mibBuilder.loadTexts:
    claRadiusServerAvpEntry.setStatus("current")
_ClaWlanId_Type = Unsigned32
_ClaWlanId_Object = MibTableColumn
claWlanId = _ClaWlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 6, 1, 1),
    _ClaWlanId_Type()
)
claWlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    claWlanId.setStatus("current")
_ClaRadiusType_Type = Unsigned32
_ClaRadiusType_Object = MibTableColumn
claRadiusType = _ClaRadiusType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 6, 1, 2),
    _ClaRadiusType_Type()
)
claRadiusType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    claRadiusType.setStatus("current")
_ClaAvpEntryId_Type = Unsigned32
_ClaAvpEntryId_Object = MibTableColumn
claAvpEntryId = _ClaAvpEntryId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 6, 1, 3),
    _ClaAvpEntryId_Type()
)
claAvpEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    claAvpEntryId.setStatus("current")
_ClaAvpVendorId_Type = Unsigned32
_ClaAvpVendorId_Object = MibTableColumn
claAvpVendorId = _ClaAvpVendorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 6, 1, 4),
    _ClaAvpVendorId_Type()
)
claAvpVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claAvpVendorId.setStatus("current")
_ClaAvpAttribute_Type = Unsigned32
_ClaAvpAttribute_Object = MibTableColumn
claAvpAttribute = _ClaAvpAttribute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 6, 1, 5),
    _ClaAvpAttribute_Type()
)
claAvpAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claAvpAttribute.setStatus("current")


class _ClaAvpType_Type(Integer32):
    """Custom type claAvpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("string", 0),
          ("char", 1),
          ("short", 2),
          ("integer", 4))
    )


_ClaAvpType_Type.__name__ = "Integer32"
_ClaAvpType_Object = MibTableColumn
claAvpType = _ClaAvpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 6, 1, 6),
    _ClaAvpType_Type()
)
claAvpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claAvpType.setStatus("current")
_ClaAvpValue_Type = DisplayString
_ClaAvpValue_Object = MibTableColumn
claAvpValue = _ClaAvpValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 2, 6, 1, 7),
    _ClaAvpValue_Type()
)
claAvpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claAvpValue.setStatus("current")
_ClaGlobalObjects_ObjectIdentity = ObjectIdentity
claGlobalObjects = _ClaGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3)
)
_ClaTacacsDnsServerEnabled_Type = TruthValue
_ClaTacacsDnsServerEnabled_Object = MibScalar
claTacacsDnsServerEnabled = _ClaTacacsDnsServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 1),
    _ClaTacacsDnsServerEnabled_Type()
)
claTacacsDnsServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claTacacsDnsServerEnabled.setStatus("current")
_ClaTacacsDnsServerAddressType_Type = InetAddressType
_ClaTacacsDnsServerAddressType_Object = MibScalar
claTacacsDnsServerAddressType = _ClaTacacsDnsServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 2),
    _ClaTacacsDnsServerAddressType_Type()
)
claTacacsDnsServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claTacacsDnsServerAddressType.setStatus("current")
_ClaTacacsDnsServerAddress_Type = InetAddress
_ClaTacacsDnsServerAddress_Object = MibScalar
claTacacsDnsServerAddress = _ClaTacacsDnsServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 3),
    _ClaTacacsDnsServerAddress_Type()
)
claTacacsDnsServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claTacacsDnsServerAddress.setStatus("current")
_ClaTacacsDnsServerPort_Type = InetPortNumber
_ClaTacacsDnsServerPort_Object = MibScalar
claTacacsDnsServerPort = _ClaTacacsDnsServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 4),
    _ClaTacacsDnsServerPort_Type()
)
claTacacsDnsServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claTacacsDnsServerPort.setStatus("current")
_ClaTacacsDnsServerSecretType_Type = CLSecKeyFormat
_ClaTacacsDnsServerSecretType_Object = MibScalar
claTacacsDnsServerSecretType = _ClaTacacsDnsServerSecretType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 5),
    _ClaTacacsDnsServerSecretType_Type()
)
claTacacsDnsServerSecretType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claTacacsDnsServerSecretType.setStatus("current")
_ClaTacacsDnsServerSecret_Type = DisplayString
_ClaTacacsDnsServerSecret_Object = MibScalar
claTacacsDnsServerSecret = _ClaTacacsDnsServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 6),
    _ClaTacacsDnsServerSecret_Type()
)
claTacacsDnsServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claTacacsDnsServerSecret.setStatus("current")
_ClaTacacsDnsServerURL_Type = CiscoURLString
_ClaTacacsDnsServerURL_Object = MibScalar
claTacacsDnsServerURL = _ClaTacacsDnsServerURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 7),
    _ClaTacacsDnsServerURL_Type()
)
claTacacsDnsServerURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claTacacsDnsServerURL.setStatus("current")
_ClaTacacsDnsServerTimeout_Type = Unsigned32
_ClaTacacsDnsServerTimeout_Object = MibScalar
claTacacsDnsServerTimeout = _ClaTacacsDnsServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 8),
    _ClaTacacsDnsServerTimeout_Type()
)
claTacacsDnsServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claTacacsDnsServerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    claTacacsDnsServerTimeout.setUnits("days")
_ClaRadiusDnsServerEnabled_Type = TruthValue
_ClaRadiusDnsServerEnabled_Object = MibScalar
claRadiusDnsServerEnabled = _ClaRadiusDnsServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 9),
    _ClaRadiusDnsServerEnabled_Type()
)
claRadiusDnsServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusDnsServerEnabled.setStatus("current")
_ClaRadiusDnsServerAddressType_Type = InetAddressType
_ClaRadiusDnsServerAddressType_Object = MibScalar
claRadiusDnsServerAddressType = _ClaRadiusDnsServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 10),
    _ClaRadiusDnsServerAddressType_Type()
)
claRadiusDnsServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusDnsServerAddressType.setStatus("current")
_ClaRadiusDnsServerAddress_Type = InetAddress
_ClaRadiusDnsServerAddress_Object = MibScalar
claRadiusDnsServerAddress = _ClaRadiusDnsServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 11),
    _ClaRadiusDnsServerAddress_Type()
)
claRadiusDnsServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusDnsServerAddress.setStatus("current")
_ClaRadiusDnsServerPort_Type = InetPortNumber
_ClaRadiusDnsServerPort_Object = MibScalar
claRadiusDnsServerPort = _ClaRadiusDnsServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 12),
    _ClaRadiusDnsServerPort_Type()
)
claRadiusDnsServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusDnsServerPort.setStatus("current")
_ClaRadiusDnsServerSecretType_Type = CLSecKeyFormat
_ClaRadiusDnsServerSecretType_Object = MibScalar
claRadiusDnsServerSecretType = _ClaRadiusDnsServerSecretType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 13),
    _ClaRadiusDnsServerSecretType_Type()
)
claRadiusDnsServerSecretType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusDnsServerSecretType.setStatus("current")
_ClaRadiusDnsServerSecret_Type = DisplayString
_ClaRadiusDnsServerSecret_Object = MibScalar
claRadiusDnsServerSecret = _ClaRadiusDnsServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 14),
    _ClaRadiusDnsServerSecret_Type()
)
claRadiusDnsServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusDnsServerSecret.setStatus("current")
_ClaRadiusDnsServerURL_Type = CiscoURLString
_ClaRadiusDnsServerURL_Object = MibScalar
claRadiusDnsServerURL = _ClaRadiusDnsServerURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 15),
    _ClaRadiusDnsServerURL_Type()
)
claRadiusDnsServerURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusDnsServerURL.setStatus("current")
_ClaRadiusDnsServerTimeout_Type = Unsigned32
_ClaRadiusDnsServerTimeout_Object = MibScalar
claRadiusDnsServerTimeout = _ClaRadiusDnsServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 16),
    _ClaRadiusDnsServerTimeout_Type()
)
claRadiusDnsServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusDnsServerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    claRadiusDnsServerTimeout.setUnits("days")


class _ClaAAARadiusAuthCallStationIdType_Type(Integer32):
    """Custom type claAAARadiusAuthCallStationIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("ipAddr", 0),
          ("macAddr", 1),
          ("apMacAddress", 2),
          ("apMacAddressSsid", 3),
          ("apNameSsid", 4),
          ("apName", 5),
          ("apGroupName", 6),
          ("flexGroupName", 7),
          ("apLocation", 8),
          ("apVlanId", 9),
          ("apMacEthAddress", 10),
          ("apMacEthAddressSsid", 11),
          ("apLabelMac", 12),
          ("apLableMacSsid", 13),
          ("apMacSsidApGroup", 14))
    )


_ClaAAARadiusAuthCallStationIdType_Type.__name__ = "Integer32"
_ClaAAARadiusAuthCallStationIdType_Object = MibScalar
claAAARadiusAuthCallStationIdType = _ClaAAARadiusAuthCallStationIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 17),
    _ClaAAARadiusAuthCallStationIdType_Type()
)
claAAARadiusAuthCallStationIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claAAARadiusAuthCallStationIdType.setStatus("current")
_ClaRadiusDnsAuthnetworkState_Type = TruthValue
_ClaRadiusDnsAuthnetworkState_Object = MibScalar
claRadiusDnsAuthnetworkState = _ClaRadiusDnsAuthnetworkState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 18),
    _ClaRadiusDnsAuthnetworkState_Type()
)
claRadiusDnsAuthnetworkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusDnsAuthnetworkState.setStatus("current")
_ClaRadiusDnsAuthmgmtState_Type = TruthValue
_ClaRadiusDnsAuthmgmtState_Object = MibScalar
claRadiusDnsAuthmgmtState = _ClaRadiusDnsAuthmgmtState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 19),
    _ClaRadiusDnsAuthmgmtState_Type()
)
claRadiusDnsAuthmgmtState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusDnsAuthmgmtState.setStatus("current")
_ClaRadiusDnsAcctnetworkState_Type = TruthValue
_ClaRadiusDnsAcctnetworkState_Object = MibScalar
claRadiusDnsAcctnetworkState = _ClaRadiusDnsAcctnetworkState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 20),
    _ClaRadiusDnsAcctnetworkState_Type()
)
claRadiusDnsAcctnetworkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusDnsAcctnetworkState.setStatus("current")


class _ClaRadiusDnsAuthRetransmitTimeout_Type(Unsigned32):
    """Custom type claRadiusDnsAuthRetransmitTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_ClaRadiusDnsAuthRetransmitTimeout_Type.__name__ = "Unsigned32"
_ClaRadiusDnsAuthRetransmitTimeout_Object = MibScalar
claRadiusDnsAuthRetransmitTimeout = _ClaRadiusDnsAuthRetransmitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 21),
    _ClaRadiusDnsAuthRetransmitTimeout_Type()
)
claRadiusDnsAuthRetransmitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusDnsAuthRetransmitTimeout.setStatus("current")


class _ClaRadiusDnsAcctRetransmitTimeout_Type(Unsigned32):
    """Custom type claRadiusDnsAcctRetransmitTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_ClaRadiusDnsAcctRetransmitTimeout_Type.__name__ = "Unsigned32"
_ClaRadiusDnsAcctRetransmitTimeout_Object = MibScalar
claRadiusDnsAcctRetransmitTimeout = _ClaRadiusDnsAcctRetransmitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 22),
    _ClaRadiusDnsAcctRetransmitTimeout_Type()
)
claRadiusDnsAcctRetransmitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusDnsAcctRetransmitTimeout.setStatus("current")
_ClaRadiusDnsAuthRfc3576State_Type = TruthValue
_ClaRadiusDnsAuthRfc3576State_Object = MibScalar
claRadiusDnsAuthRfc3576State = _ClaRadiusDnsAuthRfc3576State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 23),
    _ClaRadiusDnsAuthRfc3576State_Type()
)
claRadiusDnsAuthRfc3576State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusDnsAuthRfc3576State.setStatus("current")
_ClaRadiusFramedMtu_Type = Unsigned32
_ClaRadiusFramedMtu_Object = MibScalar
claRadiusFramedMtu = _ClaRadiusFramedMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 24),
    _ClaRadiusFramedMtu_Type()
)
claRadiusFramedMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusFramedMtu.setStatus("current")


class _ClaRadiusDnsAuthMgmtRetransmitTimeout_Type(Unsigned32):
    """Custom type claRadiusDnsAuthMgmtRetransmitTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ClaRadiusDnsAuthMgmtRetransmitTimeout_Type.__name__ = "Unsigned32"
_ClaRadiusDnsAuthMgmtRetransmitTimeout_Object = MibScalar
claRadiusDnsAuthMgmtRetransmitTimeout = _ClaRadiusDnsAuthMgmtRetransmitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 25),
    _ClaRadiusDnsAuthMgmtRetransmitTimeout_Type()
)
claRadiusDnsAuthMgmtRetransmitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claRadiusDnsAuthMgmtRetransmitTimeout.setStatus("current")
_ClaMgmtUserReauthInterval_Type = Unsigned32
_ClaMgmtUserReauthInterval_Object = MibScalar
claMgmtUserReauthInterval = _ClaMgmtUserReauthInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 1, 3, 26),
    _ClaMgmtUserReauthInterval_Type()
)
claMgmtUserReauthInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claMgmtUserReauthInterval.setStatus("current")
_CiscoLwappAAAMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappAAAMIBConform = _CiscoLwappAAAMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2)
)
_CiscoLwappAAAMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappAAAMIBCompliances = _CiscoLwappAAAMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 1)
)
_CiscoLwappAAAMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappAAAMIBGroups = _CiscoLwappAAAMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2)
)

# Managed Objects groups

ciscoLwappAAAMIBConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2, 1)
)
ciscoLwappAAAMIBConfigGroup.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "claPriorityOrder"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsServerAddressType"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsServerAddress"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsServerPortNum"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsServerEnabled"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsServerSecretType"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsServerSecret"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsServerTimeout"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsServerStorageType"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsServerRowStatus"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusServerGlobalActivatedEnabled"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusServerGlobalDeactivatedEnabled"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusServerWlanActivatedEnabled"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusServerWlanDeactivatedEnabled"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusReqTimedOutEnabled"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsDnsServerEnabled"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsDnsServerAddressType"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsDnsServerAddress"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsDnsServerPort"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsDnsServerSecretType"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsDnsServerSecret"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsDnsServerURL"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsDnsServerTimeout"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusDnsServerEnabled"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusDnsServerAddressType"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusDnsServerAddress"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusDnsServerPort"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusDnsServerSecretType"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusDnsServerSecret"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusDnsServerURL"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusDnsServerTimeout"),
        ("CISCO-LWAPP-AAA-MIB", "claAAARadiusAuthCallStationIdType"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusDnsAuthnetworkState"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusDnsAuthmgmtState"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusDnsAcctnetworkState"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusDnsAuthRetransmitTimeout"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusDnsAcctRetransmitTimeout"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusDnsAuthRfc3576State"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusFramedMtu"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusDnsAuthMgmtRetransmitTimeout"),
        ("CISCO-LWAPP-AAA-MIB", "claMgmtUserReauthInterval"),
        ("CISCO-LWAPP-AAA-MIB", "claWlanOverwriteInterface"),
        ("CISCO-LWAPP-AAA-MIB", "claWlanInterimUpdate"),
        ("CISCO-LWAPP-AAA-MIB", "claWlanInterimUpdateInterval"),
        ("CISCO-LWAPP-AAA-MIB", "claTacacsFallbackTestInterval"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAuthClientAccessRequestsTotal"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAuthClientAccessResponseTotal"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAuthClientAccessAcceptsTotal"),
        ("CISCO-LWAPP-AAA-MIB", "claWlanId"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusType"),
        ("CISCO-LWAPP-AAA-MIB", "claAvpEntryId"),
        ("CISCO-LWAPP-AAA-MIB", "claAvpVendorId"),
        ("CISCO-LWAPP-AAA-MIB", "claAvpAttribute"),
        ("CISCO-LWAPP-AAA-MIB", "claAvpType"),
        ("CISCO-LWAPP-AAA-MIB", "claAvpValue"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAAMIBConfigGroup.setStatus("current")

ciscoLwappAAAMIBSaveUserConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2, 2)
)
ciscoLwappAAAMIBSaveUserConfigGroup.setObjects(
    ("CISCO-LWAPP-AAA-MIB", "claSaveUserData")
)
if mibBuilder.loadTexts:
    ciscoLwappAAAMIBSaveUserConfigGroup.setStatus("current")

ciscoLwappAAAMIBStatusObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2, 4)
)
ciscoLwappAAAMIBStatusObjsGroup.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "claRadiusAddressType"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAddress"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusPortNum"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusWlanIdx"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusClientMacAddress"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusUserName"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAAMIBStatusObjsGroup.setStatus("current")

ciscoLwappAAAMIBDBEntriesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2, 5)
)
ciscoLwappAAAMIBDBEntriesGroup.setObjects(
    ("CISCO-LWAPP-AAA-MIB", "claDBCurrentUsedEntries")
)
if mibBuilder.loadTexts:
    ciscoLwappAAAMIBDBEntriesGroup.setStatus("current")

ciscoLwappAAAMIBRadiusConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2, 6)
)
ciscoLwappAAAMIBRadiusConfigGroup.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "claWebRadiusAuthentication"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusFallbackMode"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusFallbackUsername"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusFallbackInterval"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAuthMacDelimiter"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAcctMacDelimiter"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAuthServerIndex"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAuthServerIPSecAuthMethod"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAuthServerKey"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAuthServerKeyFormat"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAuthServerIsActive"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAuthServerPacState"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAccServerIndex"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAccServerIPSecAuthMethod"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAccServerKey"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAccServerKeyFormat"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAccServerIsActive"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAccServerTunnelProxy"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAccServerPacState"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAuthServerRealm"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAuthRealmRowStatus"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAcctServerRealm"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAcctRealmRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAAMIBRadiusConfigGroup.setStatus("current")

ciscoLwappAAAMIBAPPolicyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2, 7)
)
ciscoLwappAAAMIBAPPolicyConfigGroup.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "claAcceptMICertificate"),
        ("CISCO-LWAPP-AAA-MIB", "claAcceptLSCertificate"),
        ("CISCO-LWAPP-AAA-MIB", "claAllowAuthorizeLscApAgainstAAA"),
        ("CISCO-LWAPP-AAA-MIB", "claSscHashValidationEnabled"),
        ("CISCO-LWAPP-AAA-MIB", "claSscCertificateSubject"),
        ("CISCO-LWAPP-AAA-MIB", "claSscCertificateValidity"),
        ("CISCO-LWAPP-AAA-MIB", "claSscCertificateHashKey"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAAMIBAPPolicyConfigGroup.setStatus("current")

ciscoLwappAAAMIBWlanAuthAccServerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2, 8)
)
ciscoLwappAAAMIBWlanAuthAccServerConfigGroup.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "claWlanAuthServerEnabled"),
        ("CISCO-LWAPP-AAA-MIB", "claWlanAcctServerEnabled"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAAMIBWlanAuthAccServerConfigGroup.setStatus("current")


# Notification objects

ciscoLwappAAARadiusServerGlobalActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 0, 1)
)
ciscoLwappAAARadiusServerGlobalActivated.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "claRadiusAddressType"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAddress"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusPortNum"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAARadiusServerGlobalActivated.setStatus(
        "current"
    )

ciscoLwappAAARadiusServerGlobalDeactivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 0, 2)
)
ciscoLwappAAARadiusServerGlobalDeactivated.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "claRadiusAddressType"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAddress"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusPortNum"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAARadiusServerGlobalDeactivated.setStatus(
        "current"
    )

ciscoLwappAAARadiusServerWlanActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 0, 3)
)
ciscoLwappAAARadiusServerWlanActivated.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "claRadiusAddressType"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAddress"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusPortNum"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusWlanIdx"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAARadiusServerWlanActivated.setStatus(
        "current"
    )

ciscoLwappAAARadiusServerWlanDeactivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 0, 4)
)
ciscoLwappAAARadiusServerWlanDeactivated.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "claRadiusAddressType"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAddress"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusPortNum"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusWlanIdx"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAARadiusServerWlanDeactivated.setStatus(
        "current"
    )

ciscoLwappAAARadiusReqTimedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 0, 5)
)
ciscoLwappAAARadiusReqTimedOut.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "claRadiusAddressType"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAddress"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusPortNum"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusClientMacAddress"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusUserName"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAARadiusReqTimedOut.setStatus(
        "current"
    )

ciscoLwappAAARadiusAuthServerAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 0, 6)
)
ciscoLwappAAARadiusAuthServerAvailable.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "claRadiusAddressType"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAddress"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusPortNum"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAARadiusAuthServerAvailable.setStatus(
        "current"
    )

ciscoLwappAAARadiusAuthServerUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 0, 7)
)
ciscoLwappAAARadiusAuthServerUnavailable.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "claRadiusAddressType"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAddress"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusPortNum"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAARadiusAuthServerUnavailable.setStatus(
        "current"
    )

ciscoLwappAAARadiusAcctServerAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 0, 8)
)
ciscoLwappAAARadiusAcctServerAvailable.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "claRadiusAddressType"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAddress"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusPortNum"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAARadiusAcctServerAvailable.setStatus(
        "current"
    )

ciscoLwappAAARadiusAcctServerUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 0, 9)
)
ciscoLwappAAARadiusAcctServerUnavailable.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "claRadiusAddressType"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusAddress"),
        ("CISCO-LWAPP-AAA-MIB", "claRadiusPortNum"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAARadiusAcctServerUnavailable.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappAAAMIBNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 2, 3)
)
ciscoLwappAAAMIBNotifsGroup.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAARadiusServerGlobalActivated"),
        ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAARadiusServerGlobalDeactivated"),
        ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAARadiusServerWlanActivated"),
        ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAARadiusServerWlanDeactivated"),
        ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAARadiusReqTimedOut"),
        ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAARadiusAuthServerAvailable"),
        ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAARadiusAuthServerUnavailable"),
        ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAARadiusAcctServerAvailable"),
        ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAARadiusAcctServerUnavailable"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAAMIBNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappAAAMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 1, 1)
)
ciscoLwappAAAMIBCompliance.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAAMIBConfigGroup"),
        ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAAMIBNotifsGroup"),
        ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAAMIBStatusObjsGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAAMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappAAAMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 598, 2, 1, 2)
)
ciscoLwappAAAMIBComplianceRev1.setObjects(
      *(("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAAMIBConfigGroup"),
        ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAAMIBSaveUserConfigGroup"),
        ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAAMIBRadiusConfigGroup"),
        ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAAMIBAPPolicyConfigGroup"),
        ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAAMIBWlanAuthAccServerConfigGroup"),
        ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAAMIBNotifsGroup"),
        ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAAMIBStatusObjsGroup"),
        ("CISCO-LWAPP-AAA-MIB", "ciscoLwappAAAMIBDBEntriesGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappAAAMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-AAA-MIB",
    **{"ciscoLwappAAAMIB": ciscoLwappAAAMIB,
       "ciscoLwappAAAMIBNotifs": ciscoLwappAAAMIBNotifs,
       "ciscoLwappAAARadiusServerGlobalActivated": ciscoLwappAAARadiusServerGlobalActivated,
       "ciscoLwappAAARadiusServerGlobalDeactivated": ciscoLwappAAARadiusServerGlobalDeactivated,
       "ciscoLwappAAARadiusServerWlanActivated": ciscoLwappAAARadiusServerWlanActivated,
       "ciscoLwappAAARadiusServerWlanDeactivated": ciscoLwappAAARadiusServerWlanDeactivated,
       "ciscoLwappAAARadiusReqTimedOut": ciscoLwappAAARadiusReqTimedOut,
       "ciscoLwappAAARadiusAuthServerAvailable": ciscoLwappAAARadiusAuthServerAvailable,
       "ciscoLwappAAARadiusAuthServerUnavailable": ciscoLwappAAARadiusAuthServerUnavailable,
       "ciscoLwappAAARadiusAcctServerAvailable": ciscoLwappAAARadiusAcctServerAvailable,
       "ciscoLwappAAARadiusAcctServerUnavailable": ciscoLwappAAARadiusAcctServerUnavailable,
       "ciscoLwappAAAMIBObjects": ciscoLwappAAAMIBObjects,
       "claConfigObjects": claConfigObjects,
       "claPriorityTable": claPriorityTable,
       "claPriorityEntry": claPriorityEntry,
       "claPriorityAuth": claPriorityAuth,
       "claPriorityOrder": claPriorityOrder,
       "claTacacsServerTable": claTacacsServerTable,
       "claTacacsServerEntry": claTacacsServerEntry,
       "claTacacsServerType": claTacacsServerType,
       "claTacacsServerPriority": claTacacsServerPriority,
       "claTacacsServerAddressType": claTacacsServerAddressType,
       "claTacacsServerAddress": claTacacsServerAddress,
       "claTacacsServerPortNum": claTacacsServerPortNum,
       "claTacacsServerEnabled": claTacacsServerEnabled,
       "claTacacsServerSecretType": claTacacsServerSecretType,
       "claTacacsServerSecret": claTacacsServerSecret,
       "claTacacsServerTimeout": claTacacsServerTimeout,
       "claTacacsServerStorageType": claTacacsServerStorageType,
       "claTacacsServerRowStatus": claTacacsServerRowStatus,
       "claWlanTable": claWlanTable,
       "claWlanEntry": claWlanEntry,
       "claWlanAcctServerEnabled": claWlanAcctServerEnabled,
       "claWlanAuthServerEnabled": claWlanAuthServerEnabled,
       "claWlanOverwriteInterface": claWlanOverwriteInterface,
       "claWlanInterimUpdate": claWlanInterimUpdate,
       "claWlanInterimUpdateInterval": claWlanInterimUpdateInterval,
       "claRadiusServerGlobalActivatedEnabled": claRadiusServerGlobalActivatedEnabled,
       "claRadiusServerGlobalDeactivatedEnabled": claRadiusServerGlobalDeactivatedEnabled,
       "claRadiusServerWlanActivatedEnabled": claRadiusServerWlanActivatedEnabled,
       "claRadiusServerWlanDeactivatedEnabled": claRadiusServerWlanDeactivatedEnabled,
       "claRadiusReqTimedOutEnabled": claRadiusReqTimedOutEnabled,
       "claSaveUserData": claSaveUserData,
       "claWebRadiusAuthentication": claWebRadiusAuthentication,
       "claRadiusFallbackMode": claRadiusFallbackMode,
       "claRadiusFallbackUsername": claRadiusFallbackUsername,
       "claRadiusFallbackInterval": claRadiusFallbackInterval,
       "claRadiusAuthMacDelimiter": claRadiusAuthMacDelimiter,
       "claRadiusAcctMacDelimiter": claRadiusAcctMacDelimiter,
       "claAcceptMICertificate": claAcceptMICertificate,
       "claAcceptLSCertificate": claAcceptLSCertificate,
       "claAllowAuthorizeLscApAgainstAAA": claAllowAuthorizeLscApAgainstAAA,
       "claSscHashValidationEnabled": claSscHashValidationEnabled,
       "claSscCertificateSubject": claSscCertificateSubject,
       "claSscCertificateValidity": claSscCertificateValidity,
       "claSscCertificateHashKey": claSscCertificateHashKey,
       "claRadiusAuthServerTable": claRadiusAuthServerTable,
       "claRadiusAuthServerEntry": claRadiusAuthServerEntry,
       "claRadiusAuthServerIndex": claRadiusAuthServerIndex,
       "claRadiusAuthServerIPSecAuthMethod": claRadiusAuthServerIPSecAuthMethod,
       "claRadiusAuthServerKey": claRadiusAuthServerKey,
       "claRadiusAuthServerKeyFormat": claRadiusAuthServerKeyFormat,
       "claRadiusAuthServerIsActive": claRadiusAuthServerIsActive,
       "claRadiusAuthServerTunnelProxy": claRadiusAuthServerTunnelProxy,
       "claRadiusAuthServerPacState": claRadiusAuthServerPacState,
       "claRadiusAccServerTable": claRadiusAccServerTable,
       "claRadiusAccServerEntry": claRadiusAccServerEntry,
       "claRadiusAccServerIndex": claRadiusAccServerIndex,
       "claRadiusAccServerIPSecAuthMethod": claRadiusAccServerIPSecAuthMethod,
       "claRadiusAccServerKey": claRadiusAccServerKey,
       "claRadiusAccServerKeyFormat": claRadiusAccServerKeyFormat,
       "claRadiusAccServerIsActive": claRadiusAccServerIsActive,
       "claRadiusAccServerTunnelProxy": claRadiusAccServerTunnelProxy,
       "claRadiusAccServerPacState": claRadiusAccServerPacState,
       "claRadiusAuthServerRealmTable": claRadiusAuthServerRealmTable,
       "claRadiusAuthServerRealmEntry": claRadiusAuthServerRealmEntry,
       "claRadiusAuthServerRealm": claRadiusAuthServerRealm,
       "claRadiusAuthRealmRowStatus": claRadiusAuthRealmRowStatus,
       "claRadiusAcctServerRealmTable": claRadiusAcctServerRealmTable,
       "claRadiusAcctServerRealmEntry": claRadiusAcctServerRealmEntry,
       "claRadiusAcctServerRealm": claRadiusAcctServerRealm,
       "claRadiusAcctRealmRowStatus": claRadiusAcctRealmRowStatus,
       "claTacacsFallbackTestInterval": claTacacsFallbackTestInterval,
       "claStatusObjects": claStatusObjects,
       "claRadiusServerTable": claRadiusServerTable,
       "claRadiusServerEntry": claRadiusServerEntry,
       "claRadiusReqId": claRadiusReqId,
       "claRadiusAddressType": claRadiusAddressType,
       "claRadiusAddress": claRadiusAddress,
       "claRadiusPortNum": claRadiusPortNum,
       "claRadiusWlanIdx": claRadiusWlanIdx,
       "claRadiusClientMacAddress": claRadiusClientMacAddress,
       "claRadiusUserName": claRadiusUserName,
       "claDBCurrentUsedEntries": claDBCurrentUsedEntries,
       "claRadiusAuthClientAccessRequestsTotal": claRadiusAuthClientAccessRequestsTotal,
       "claRadiusAuthClientAccessResponseTotal": claRadiusAuthClientAccessResponseTotal,
       "claRadiusAuthClientAccessAcceptsTotal": claRadiusAuthClientAccessAcceptsTotal,
       "claRadiusServerAvpTable": claRadiusServerAvpTable,
       "claRadiusServerAvpEntry": claRadiusServerAvpEntry,
       "claWlanId": claWlanId,
       "claRadiusType": claRadiusType,
       "claAvpEntryId": claAvpEntryId,
       "claAvpVendorId": claAvpVendorId,
       "claAvpAttribute": claAvpAttribute,
       "claAvpType": claAvpType,
       "claAvpValue": claAvpValue,
       "claGlobalObjects": claGlobalObjects,
       "claTacacsDnsServerEnabled": claTacacsDnsServerEnabled,
       "claTacacsDnsServerAddressType": claTacacsDnsServerAddressType,
       "claTacacsDnsServerAddress": claTacacsDnsServerAddress,
       "claTacacsDnsServerPort": claTacacsDnsServerPort,
       "claTacacsDnsServerSecretType": claTacacsDnsServerSecretType,
       "claTacacsDnsServerSecret": claTacacsDnsServerSecret,
       "claTacacsDnsServerURL": claTacacsDnsServerURL,
       "claTacacsDnsServerTimeout": claTacacsDnsServerTimeout,
       "claRadiusDnsServerEnabled": claRadiusDnsServerEnabled,
       "claRadiusDnsServerAddressType": claRadiusDnsServerAddressType,
       "claRadiusDnsServerAddress": claRadiusDnsServerAddress,
       "claRadiusDnsServerPort": claRadiusDnsServerPort,
       "claRadiusDnsServerSecretType": claRadiusDnsServerSecretType,
       "claRadiusDnsServerSecret": claRadiusDnsServerSecret,
       "claRadiusDnsServerURL": claRadiusDnsServerURL,
       "claRadiusDnsServerTimeout": claRadiusDnsServerTimeout,
       "claAAARadiusAuthCallStationIdType": claAAARadiusAuthCallStationIdType,
       "claRadiusDnsAuthnetworkState": claRadiusDnsAuthnetworkState,
       "claRadiusDnsAuthmgmtState": claRadiusDnsAuthmgmtState,
       "claRadiusDnsAcctnetworkState": claRadiusDnsAcctnetworkState,
       "claRadiusDnsAuthRetransmitTimeout": claRadiusDnsAuthRetransmitTimeout,
       "claRadiusDnsAcctRetransmitTimeout": claRadiusDnsAcctRetransmitTimeout,
       "claRadiusDnsAuthRfc3576State": claRadiusDnsAuthRfc3576State,
       "claRadiusFramedMtu": claRadiusFramedMtu,
       "claRadiusDnsAuthMgmtRetransmitTimeout": claRadiusDnsAuthMgmtRetransmitTimeout,
       "claMgmtUserReauthInterval": claMgmtUserReauthInterval,
       "ciscoLwappAAAMIBConform": ciscoLwappAAAMIBConform,
       "ciscoLwappAAAMIBCompliances": ciscoLwappAAAMIBCompliances,
       "ciscoLwappAAAMIBCompliance": ciscoLwappAAAMIBCompliance,
       "ciscoLwappAAAMIBComplianceRev1": ciscoLwappAAAMIBComplianceRev1,
       "ciscoLwappAAAMIBGroups": ciscoLwappAAAMIBGroups,
       "ciscoLwappAAAMIBConfigGroup": ciscoLwappAAAMIBConfigGroup,
       "ciscoLwappAAAMIBSaveUserConfigGroup": ciscoLwappAAAMIBSaveUserConfigGroup,
       "ciscoLwappAAAMIBNotifsGroup": ciscoLwappAAAMIBNotifsGroup,
       "ciscoLwappAAAMIBStatusObjsGroup": ciscoLwappAAAMIBStatusObjsGroup,
       "ciscoLwappAAAMIBDBEntriesGroup": ciscoLwappAAAMIBDBEntriesGroup,
       "ciscoLwappAAAMIBRadiusConfigGroup": ciscoLwappAAAMIBRadiusConfigGroup,
       "ciscoLwappAAAMIBAPPolicyConfigGroup": ciscoLwappAAAMIBAPPolicyConfigGroup,
       "ciscoLwappAAAMIBWlanAuthAccServerConfigGroup": ciscoLwappAAAMIBWlanAuthAccServerConfigGroup}
)
