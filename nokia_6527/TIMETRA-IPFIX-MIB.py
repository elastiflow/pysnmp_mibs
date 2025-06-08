# SNMP MIB module (TIMETRA-IPFIX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-IPFIX-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:44:24 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TItemDescription,
 TNamedItem,
 TmnxAdminState,
 TmnxVRtrID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TmnxAdminState",
    "TmnxVRtrID")

(vRtrID,) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID")


# MODULE-IDENTITY

timetraIpfixMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 78)
)
if mibBuilder.loadTexts:
    timetraIpfixMIBModule.setRevisions(
        ("2012-02-28 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxIpfixConformance_ObjectIdentity = ObjectIdentity
tmnxIpfixConformance = _TmnxIpfixConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 78)
)
_TmnxIpfixCompliances_ObjectIdentity = ObjectIdentity
tmnxIpfixCompliances = _TmnxIpfixCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 78, 1)
)
_TmnxIpfixGroups_ObjectIdentity = ObjectIdentity
tmnxIpfixGroups = _TmnxIpfixGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 78, 2)
)
_TmnxIpfix_ObjectIdentity = ObjectIdentity
tmnxIpfix = _TmnxIpfix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 78)
)
_TmnxIpfixObjs_ObjectIdentity = ObjectIdentity
tmnxIpfixObjs = _TmnxIpfixObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 78, 1)
)
_TmnxIpfixExportObjs_ObjectIdentity = ObjectIdentity
tmnxIpfixExportObjs = _TmnxIpfixExportObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 78, 1, 1)
)
_TmnxIpfixExpPlcyTable_Object = MibTable
tmnxIpfixExpPlcyTable = _TmnxIpfixExpPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 78, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxIpfixExpPlcyTable.setStatus("current")
_TmnxIpfixExpPlcyEntry_Object = MibTableRow
tmnxIpfixExpPlcyEntry = _TmnxIpfixExpPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 78, 1, 1, 1, 1)
)
tmnxIpfixExpPlcyEntry.setIndexNames(
    (1, "TIMETRA-IPFIX-MIB", "tmnxIpfixExpPlcyName"),
)
if mibBuilder.loadTexts:
    tmnxIpfixExpPlcyEntry.setStatus("current")
_TmnxIpfixExpPlcyName_Type = TNamedItem
_TmnxIpfixExpPlcyName_Object = MibTableColumn
tmnxIpfixExpPlcyName = _TmnxIpfixExpPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 78, 1, 1, 1, 1, 1),
    _TmnxIpfixExpPlcyName_Type()
)
tmnxIpfixExpPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIpfixExpPlcyName.setStatus("current")
_TmnxIpfixExpPlcyLastCh_Type = TimeStamp
_TmnxIpfixExpPlcyLastCh_Object = MibTableColumn
tmnxIpfixExpPlcyLastCh = _TmnxIpfixExpPlcyLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 78, 1, 1, 1, 1, 2),
    _TmnxIpfixExpPlcyLastCh_Type()
)
tmnxIpfixExpPlcyLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIpfixExpPlcyLastCh.setStatus("current")
_TmnxIpfixExpPlcyRowStatus_Type = RowStatus
_TmnxIpfixExpPlcyRowStatus_Object = MibTableColumn
tmnxIpfixExpPlcyRowStatus = _TmnxIpfixExpPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 78, 1, 1, 1, 1, 3),
    _TmnxIpfixExpPlcyRowStatus_Type()
)
tmnxIpfixExpPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIpfixExpPlcyRowStatus.setStatus("current")


class _TmnxIpfixExpPlcyDescription_Type(TItemDescription):
    """Custom type tmnxIpfixExpPlcyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxIpfixExpPlcyDescription_Type.__name__ = "TItemDescription"
_TmnxIpfixExpPlcyDescription_Object = MibTableColumn
tmnxIpfixExpPlcyDescription = _TmnxIpfixExpPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 78, 1, 1, 1, 1, 4),
    _TmnxIpfixExpPlcyDescription_Type()
)
tmnxIpfixExpPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIpfixExpPlcyDescription.setStatus("current")
_TmnxIpfixExpPlcyColTable_Object = MibTable
tmnxIpfixExpPlcyColTable = _TmnxIpfixExpPlcyColTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 78, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxIpfixExpPlcyColTable.setStatus("current")
_TmnxIpfixExpPlcyColEntry_Object = MibTableRow
tmnxIpfixExpPlcyColEntry = _TmnxIpfixExpPlcyColEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 78, 1, 1, 2, 1)
)
tmnxIpfixExpPlcyColEntry.setIndexNames(
    (0, "TIMETRA-IPFIX-MIB", "tmnxIpfixExpPlcyName"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-IPFIX-MIB", "tmnxIpfixExpPlcyColAddrType"),
    (0, "TIMETRA-IPFIX-MIB", "tmnxIpfixExpPlcyColAddr"),
)
if mibBuilder.loadTexts:
    tmnxIpfixExpPlcyColEntry.setStatus("current")
_TmnxIpfixExpPlcyColAddrType_Type = InetAddressType
_TmnxIpfixExpPlcyColAddrType_Object = MibTableColumn
tmnxIpfixExpPlcyColAddrType = _TmnxIpfixExpPlcyColAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 78, 1, 1, 2, 1, 1),
    _TmnxIpfixExpPlcyColAddrType_Type()
)
tmnxIpfixExpPlcyColAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIpfixExpPlcyColAddrType.setStatus("current")


class _TmnxIpfixExpPlcyColAddr_Type(InetAddress):
    """Custom type tmnxIpfixExpPlcyColAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxIpfixExpPlcyColAddr_Type.__name__ = "InetAddress"
_TmnxIpfixExpPlcyColAddr_Object = MibTableColumn
tmnxIpfixExpPlcyColAddr = _TmnxIpfixExpPlcyColAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 78, 1, 1, 2, 1, 2),
    _TmnxIpfixExpPlcyColAddr_Type()
)
tmnxIpfixExpPlcyColAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIpfixExpPlcyColAddr.setStatus("current")
_TmnxIpfixExpPlcyColRowStatus_Type = RowStatus
_TmnxIpfixExpPlcyColRowStatus_Object = MibTableColumn
tmnxIpfixExpPlcyColRowStatus = _TmnxIpfixExpPlcyColRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 78, 1, 1, 2, 1, 3),
    _TmnxIpfixExpPlcyColRowStatus_Type()
)
tmnxIpfixExpPlcyColRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIpfixExpPlcyColRowStatus.setStatus("current")
_TmnxIpfixExpPlcyColLastCh_Type = TimeStamp
_TmnxIpfixExpPlcyColLastCh_Object = MibTableColumn
tmnxIpfixExpPlcyColLastCh = _TmnxIpfixExpPlcyColLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 78, 1, 1, 2, 1, 4),
    _TmnxIpfixExpPlcyColLastCh_Type()
)
tmnxIpfixExpPlcyColLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIpfixExpPlcyColLastCh.setStatus("current")


class _TmnxIpfixExpPlcyColAdminState_Type(TmnxAdminState):
    """Custom type tmnxIpfixExpPlcyColAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxIpfixExpPlcyColAdminState_Type.__name__ = "TmnxAdminState"
_TmnxIpfixExpPlcyColAdminState_Object = MibTableColumn
tmnxIpfixExpPlcyColAdminState = _TmnxIpfixExpPlcyColAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 78, 1, 1, 2, 1, 5),
    _TmnxIpfixExpPlcyColAdminState_Type()
)
tmnxIpfixExpPlcyColAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIpfixExpPlcyColAdminState.setStatus("current")


class _TmnxIpfixExpPlcyColSrcAddrType_Type(InetAddressType):
    """Custom type tmnxIpfixExpPlcyColSrcAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIpfixExpPlcyColSrcAddrType_Type.__name__ = "InetAddressType"
_TmnxIpfixExpPlcyColSrcAddrType_Object = MibTableColumn
tmnxIpfixExpPlcyColSrcAddrType = _TmnxIpfixExpPlcyColSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 78, 1, 1, 2, 1, 6),
    _TmnxIpfixExpPlcyColSrcAddrType_Type()
)
tmnxIpfixExpPlcyColSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIpfixExpPlcyColSrcAddrType.setStatus("current")


class _TmnxIpfixExpPlcyColSrcAddr_Type(InetAddress):
    """Custom type tmnxIpfixExpPlcyColSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxIpfixExpPlcyColSrcAddr_Type.__name__ = "InetAddress"
_TmnxIpfixExpPlcyColSrcAddr_Object = MibTableColumn
tmnxIpfixExpPlcyColSrcAddr = _TmnxIpfixExpPlcyColSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 78, 1, 1, 2, 1, 7),
    _TmnxIpfixExpPlcyColSrcAddr_Type()
)
tmnxIpfixExpPlcyColSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIpfixExpPlcyColSrcAddr.setStatus("current")


class _TmnxIpfixExpPlcyColMtu_Type(Unsigned32):
    """Custom type tmnxIpfixExpPlcyColMtu based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 9212),
    )


_TmnxIpfixExpPlcyColMtu_Type.__name__ = "Unsigned32"
_TmnxIpfixExpPlcyColMtu_Object = MibTableColumn
tmnxIpfixExpPlcyColMtu = _TmnxIpfixExpPlcyColMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 78, 1, 1, 2, 1, 8),
    _TmnxIpfixExpPlcyColMtu_Type()
)
tmnxIpfixExpPlcyColMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIpfixExpPlcyColMtu.setStatus("current")


class _TmnxIpfixExpPlcyColTmplRefrshTo_Type(Unsigned32):
    """Custom type tmnxIpfixExpPlcyColTmplRefrshTo based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(240, 86400),
    )


_TmnxIpfixExpPlcyColTmplRefrshTo_Type.__name__ = "Unsigned32"
_TmnxIpfixExpPlcyColTmplRefrshTo_Object = MibTableColumn
tmnxIpfixExpPlcyColTmplRefrshTo = _TmnxIpfixExpPlcyColTmplRefrshTo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 78, 1, 1, 2, 1, 9),
    _TmnxIpfixExpPlcyColTmplRefrshTo_Type()
)
tmnxIpfixExpPlcyColTmplRefrshTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIpfixExpPlcyColTmplRefrshTo.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIpfixExpPlcyColTmplRefrshTo.setUnits("seconds")
_TmnxIpfixExpPlcyTableCh_Type = TimeStamp
_TmnxIpfixExpPlcyTableCh_Object = MibScalar
tmnxIpfixExpPlcyTableCh = _TmnxIpfixExpPlcyTableCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 78, 1, 100),
    _TmnxIpfixExpPlcyTableCh_Type()
)
tmnxIpfixExpPlcyTableCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIpfixExpPlcyTableCh.setStatus("current")
_TmnxIpfixExpPlcyColTableCh_Type = TimeStamp
_TmnxIpfixExpPlcyColTableCh_Object = MibScalar
tmnxIpfixExpPlcyColTableCh = _TmnxIpfixExpPlcyColTableCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 78, 1, 101),
    _TmnxIpfixExpPlcyColTableCh_Type()
)
tmnxIpfixExpPlcyColTableCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIpfixExpPlcyColTableCh.setStatus("current")
_TmnxIpfixNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxIpfixNotifyPrefix = _TmnxIpfixNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 78)
)
_TmnxIpfixNotifications_ObjectIdentity = ObjectIdentity
tmnxIpfixNotifications = _TmnxIpfixNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 78, 0)
)

# Managed Objects groups

tmnxIpfixExportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 78, 2, 1)
)
tmnxIpfixExportGroup.setObjects(
      *(("TIMETRA-IPFIX-MIB", "tmnxIpfixExpPlcyTableCh"),
        ("TIMETRA-IPFIX-MIB", "tmnxIpfixExpPlcyLastCh"),
        ("TIMETRA-IPFIX-MIB", "tmnxIpfixExpPlcyRowStatus"),
        ("TIMETRA-IPFIX-MIB", "tmnxIpfixExpPlcyDescription"),
        ("TIMETRA-IPFIX-MIB", "tmnxIpfixExpPlcyColTableCh"),
        ("TIMETRA-IPFIX-MIB", "tmnxIpfixExpPlcyColRowStatus"),
        ("TIMETRA-IPFIX-MIB", "tmnxIpfixExpPlcyColLastCh"),
        ("TIMETRA-IPFIX-MIB", "tmnxIpfixExpPlcyColAdminState"),
        ("TIMETRA-IPFIX-MIB", "tmnxIpfixExpPlcyColSrcAddrType"),
        ("TIMETRA-IPFIX-MIB", "tmnxIpfixExpPlcyColSrcAddr"),
        ("TIMETRA-IPFIX-MIB", "tmnxIpfixExpPlcyColMtu"),
        ("TIMETRA-IPFIX-MIB", "tmnxIpfixExpPlcyColTmplRefrshTo"))
)
if mibBuilder.loadTexts:
    tmnxIpfixExportGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmnxIpfixCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 78, 1, 1)
)
tmnxIpfixCompliance.setObjects(
    ("TIMETRA-IPFIX-MIB", "tmnxIpfixExportGroup")
)
if mibBuilder.loadTexts:
    tmnxIpfixCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-IPFIX-MIB",
    **{"timetraIpfixMIBModule": timetraIpfixMIBModule,
       "tmnxIpfixConformance": tmnxIpfixConformance,
       "tmnxIpfixCompliances": tmnxIpfixCompliances,
       "tmnxIpfixCompliance": tmnxIpfixCompliance,
       "tmnxIpfixGroups": tmnxIpfixGroups,
       "tmnxIpfixExportGroup": tmnxIpfixExportGroup,
       "tmnxIpfix": tmnxIpfix,
       "tmnxIpfixObjs": tmnxIpfixObjs,
       "tmnxIpfixExportObjs": tmnxIpfixExportObjs,
       "tmnxIpfixExpPlcyTable": tmnxIpfixExpPlcyTable,
       "tmnxIpfixExpPlcyEntry": tmnxIpfixExpPlcyEntry,
       "tmnxIpfixExpPlcyName": tmnxIpfixExpPlcyName,
       "tmnxIpfixExpPlcyLastCh": tmnxIpfixExpPlcyLastCh,
       "tmnxIpfixExpPlcyRowStatus": tmnxIpfixExpPlcyRowStatus,
       "tmnxIpfixExpPlcyDescription": tmnxIpfixExpPlcyDescription,
       "tmnxIpfixExpPlcyColTable": tmnxIpfixExpPlcyColTable,
       "tmnxIpfixExpPlcyColEntry": tmnxIpfixExpPlcyColEntry,
       "tmnxIpfixExpPlcyColAddrType": tmnxIpfixExpPlcyColAddrType,
       "tmnxIpfixExpPlcyColAddr": tmnxIpfixExpPlcyColAddr,
       "tmnxIpfixExpPlcyColRowStatus": tmnxIpfixExpPlcyColRowStatus,
       "tmnxIpfixExpPlcyColLastCh": tmnxIpfixExpPlcyColLastCh,
       "tmnxIpfixExpPlcyColAdminState": tmnxIpfixExpPlcyColAdminState,
       "tmnxIpfixExpPlcyColSrcAddrType": tmnxIpfixExpPlcyColSrcAddrType,
       "tmnxIpfixExpPlcyColSrcAddr": tmnxIpfixExpPlcyColSrcAddr,
       "tmnxIpfixExpPlcyColMtu": tmnxIpfixExpPlcyColMtu,
       "tmnxIpfixExpPlcyColTmplRefrshTo": tmnxIpfixExpPlcyColTmplRefrshTo,
       "tmnxIpfixExpPlcyTableCh": tmnxIpfixExpPlcyTableCh,
       "tmnxIpfixExpPlcyColTableCh": tmnxIpfixExpPlcyColTableCh,
       "tmnxIpfixNotifyPrefix": tmnxIpfixNotifyPrefix,
       "tmnxIpfixNotifications": tmnxIpfixNotifications}
)
