# SNMP MIB module (TROPIC-GMPLS-NE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-GMPLS-NE-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:04:18 2025
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
 InetAddressIPv4,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(tnGmplsMIBModules,
 tnGmplsObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnGmplsMIBModules",
    "tnGmplsObjs")


# MODULE-IDENTITY

tnGmplsNeMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 6, 4)
)
if mibBuilder.loadTexts:
    tnGmplsNeMibModule.setRevisions(
        ("2013-06-27 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnGmplsNeMIB_ObjectIdentity = ObjectIdentity
tnGmplsNeMIB = _TnGmplsNeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4)
)
_TnGmplsNeObjs_ObjectIdentity = ObjectIdentity
tnGmplsNeObjs = _TnGmplsNeObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1)
)
_TnGmplsNeAttributeTotal_Type = Integer32
_TnGmplsNeAttributeTotal_Object = MibScalar
tnGmplsNeAttributeTotal = _TnGmplsNeAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 1),
    _TnGmplsNeAttributeTotal_Type()
)
tnGmplsNeAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsNeAttributeTotal.setStatus("current")
_TnGmplsNeTable_Object = MibTable
tnGmplsNeTable = _TnGmplsNeTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    tnGmplsNeTable.setStatus("current")
_TnGmplsNeEntry_Object = MibTableRow
tnGmplsNeEntry = _TnGmplsNeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 2, 1)
)
tnGmplsNeEntry.setIndexNames(
    (0, "TROPIC-GMPLS-NE-MIB", "tnGmplsNeIndex"),
)
if mibBuilder.loadTexts:
    tnGmplsNeEntry.setStatus("current")
_TnGmplsNeIndex_Type = Unsigned32
_TnGmplsNeIndex_Object = MibTableColumn
tnGmplsNeIndex = _TnGmplsNeIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 2, 1, 1),
    _TnGmplsNeIndex_Type()
)
tnGmplsNeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsNeIndex.setStatus("current")
_TnGmplsNeCPNodeId_Type = InetAddressIPv4
_TnGmplsNeCPNodeId_Object = MibTableColumn
tnGmplsNeCPNodeId = _TnGmplsNeCPNodeId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 2, 1, 2),
    _TnGmplsNeCPNodeId_Type()
)
tnGmplsNeCPNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsNeCPNodeId.setStatus("current")
_TnGmplsNeNodeAddrType_Type = InetAddressType
_TnGmplsNeNodeAddrType_Object = MibTableColumn
tnGmplsNeNodeAddrType = _TnGmplsNeNodeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 2, 1, 3),
    _TnGmplsNeNodeAddrType_Type()
)
tnGmplsNeNodeAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsNeNodeAddrType.setStatus("current")
_TnGmplsNeNodeAddr_Type = InetAddress
_TnGmplsNeNodeAddr_Object = MibTableColumn
tnGmplsNeNodeAddr = _TnGmplsNeNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 2, 1, 4),
    _TnGmplsNeNodeAddr_Type()
)
tnGmplsNeNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsNeNodeAddr.setStatus("current")
_TnGmplsNeNotifyAddrType_Type = InetAddressType
_TnGmplsNeNotifyAddrType_Object = MibTableColumn
tnGmplsNeNotifyAddrType = _TnGmplsNeNotifyAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 2, 1, 5),
    _TnGmplsNeNotifyAddrType_Type()
)
tnGmplsNeNotifyAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsNeNotifyAddrType.setStatus("current")
_TnGmplsNeNotifyAddr_Type = InetAddress
_TnGmplsNeNotifyAddr_Object = MibTableColumn
tnGmplsNeNotifyAddr = _TnGmplsNeNotifyAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 2, 1, 6),
    _TnGmplsNeNotifyAddr_Type()
)
tnGmplsNeNotifyAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsNeNotifyAddr.setStatus("current")
_TnGmplsNeNodeName_Type = DisplayString
_TnGmplsNeNodeName_Object = MibTableColumn
tnGmplsNeNodeName = _TnGmplsNeNodeName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 2, 1, 7),
    _TnGmplsNeNodeName_Type()
)
tnGmplsNeNodeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsNeNodeName.setStatus("current")
_TnGmplsNeDcnOspfArea_Type = InetAddressIPv4
_TnGmplsNeDcnOspfArea_Object = MibTableColumn
tnGmplsNeDcnOspfArea = _TnGmplsNeDcnOspfArea_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 2, 1, 8),
    _TnGmplsNeDcnOspfArea_Type()
)
tnGmplsNeDcnOspfArea.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsNeDcnOspfArea.setStatus("current")


class _TnGmplsNeRestorationMode_Type(Integer32):
    """Custom type tnGmplsNeRestorationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2),
          ("prio2", 3),
          ("prio3", 4),
          ("prio4", 5),
          ("prio5", 6))
    )


_TnGmplsNeRestorationMode_Type.__name__ = "Integer32"
_TnGmplsNeRestorationMode_Object = MibTableColumn
tnGmplsNeRestorationMode = _TnGmplsNeRestorationMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 2, 1, 9),
    _TnGmplsNeRestorationMode_Type()
)
tnGmplsNeRestorationMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsNeRestorationMode.setStatus("current")


class _TnGmplsNeAutomode_Type(Integer32):
    """Custom type tnGmplsNeAutomode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("managed", 2),
          ("full", 3))
    )


_TnGmplsNeAutomode_Type.__name__ = "Integer32"
_TnGmplsNeAutomode_Object = MibTableColumn
tnGmplsNeAutomode = _TnGmplsNeAutomode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 2, 1, 10),
    _TnGmplsNeAutomode_Type()
)
tnGmplsNeAutomode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsNeAutomode.setStatus("current")
_TnGmplsNeActiveNWVersion_Type = DisplayString
_TnGmplsNeActiveNWVersion_Object = MibTableColumn
tnGmplsNeActiveNWVersion = _TnGmplsNeActiveNWVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 2, 1, 11),
    _TnGmplsNeActiveNWVersion_Type()
)
tnGmplsNeActiveNWVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsNeActiveNWVersion.setStatus("current")
_TnGmplsNeInstalledNWVersion_Type = DisplayString
_TnGmplsNeInstalledNWVersion_Object = MibTableColumn
tnGmplsNeInstalledNWVersion = _TnGmplsNeInstalledNWVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 2, 1, 12),
    _TnGmplsNeInstalledNWVersion_Type()
)
tnGmplsNeInstalledNWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsNeInstalledNWVersion.setStatus("current")


class _TnGmplsNeAdminStatus_Type(Integer32):
    """Custom type tnGmplsNeAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_TnGmplsNeAdminStatus_Type.__name__ = "Integer32"
_TnGmplsNeAdminStatus_Object = MibTableColumn
tnGmplsNeAdminStatus = _TnGmplsNeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 2, 1, 13),
    _TnGmplsNeAdminStatus_Type()
)
tnGmplsNeAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsNeAdminStatus.setStatus("current")


class _TnGmplsNeOperationalState_Type(Integer32):
    """Custom type tnGmplsNeOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("degraded", 2),
          ("up", 3))
    )


_TnGmplsNeOperationalState_Type.__name__ = "Integer32"
_TnGmplsNeOperationalState_Object = MibTableColumn
tnGmplsNeOperationalState = _TnGmplsNeOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 2, 1, 14),
    _TnGmplsNeOperationalState_Type()
)
tnGmplsNeOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmplsNeOperationalState.setStatus("current")
_TnGmplsNeColocatedNodeAddrType_Type = InetAddressType
_TnGmplsNeColocatedNodeAddrType_Object = MibTableColumn
tnGmplsNeColocatedNodeAddrType = _TnGmplsNeColocatedNodeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 2, 1, 15),
    _TnGmplsNeColocatedNodeAddrType_Type()
)
tnGmplsNeColocatedNodeAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsNeColocatedNodeAddrType.setStatus("current")
_TnGmplsNeColocatedNode_Type = InetAddress
_TnGmplsNeColocatedNode_Object = MibTableColumn
tnGmplsNeColocatedNode = _TnGmplsNeColocatedNode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 2, 1, 16),
    _TnGmplsNeColocatedNode_Type()
)
tnGmplsNeColocatedNode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsNeColocatedNode.setStatus("current")
_TnGmplsNeRowStatus_Type = RowStatus
_TnGmplsNeRowStatus_Object = MibTableColumn
tnGmplsNeRowStatus = _TnGmplsNeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 2, 1, 17),
    _TnGmplsNeRowStatus_Type()
)
tnGmplsNeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsNeRowStatus.setStatus("current")
_TnGmplsNeSubnodeTable_Object = MibTable
tnGmplsNeSubnodeTable = _TnGmplsNeSubnodeTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    tnGmplsNeSubnodeTable.setStatus("current")
_TnGmplsNeSubnodeEntry_Object = MibTableRow
tnGmplsNeSubnodeEntry = _TnGmplsNeSubnodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 3, 1)
)
tnGmplsNeSubnodeEntry.setIndexNames(
    (0, "TROPIC-GMPLS-NE-MIB", "tnGmplsNeSubnodeIndex"),
)
if mibBuilder.loadTexts:
    tnGmplsNeSubnodeEntry.setStatus("current")
_TnGmplsNeSubnodeIndex_Type = Unsigned32
_TnGmplsNeSubnodeIndex_Object = MibTableColumn
tnGmplsNeSubnodeIndex = _TnGmplsNeSubnodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 3, 1, 1),
    _TnGmplsNeSubnodeIndex_Type()
)
tnGmplsNeSubnodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmplsNeSubnodeIndex.setStatus("current")
_TnGmplsNeSubnodeId_Type = Unsigned32
_TnGmplsNeSubnodeId_Object = MibTableColumn
tnGmplsNeSubnodeId = _TnGmplsNeSubnodeId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 3, 1, 2),
    _TnGmplsNeSubnodeId_Type()
)
tnGmplsNeSubnodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsNeSubnodeId.setStatus("current")


class _TnGmplsNeSubnodeAdminStatus_Type(Integer32):
    """Custom type tnGmplsNeSubnodeAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_TnGmplsNeSubnodeAdminStatus_Type.__name__ = "Integer32"
_TnGmplsNeSubnodeAdminStatus_Object = MibTableColumn
tnGmplsNeSubnodeAdminStatus = _TnGmplsNeSubnodeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 3, 1, 3),
    _TnGmplsNeSubnodeAdminStatus_Type()
)
tnGmplsNeSubnodeAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsNeSubnodeAdminStatus.setStatus("current")
_TnGmplsNeSubnodeRowStatus_Type = RowStatus
_TnGmplsNeSubnodeRowStatus_Object = MibTableColumn
tnGmplsNeSubnodeRowStatus = _TnGmplsNeSubnodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 1, 3, 1, 4),
    _TnGmplsNeSubnodeRowStatus_Type()
)
tnGmplsNeSubnodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmplsNeSubnodeRowStatus.setStatus("current")
_TnGmplsNeConf_ObjectIdentity = ObjectIdentity
tnGmplsNeConf = _TnGmplsNeConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 3)
)
_TnGmplsNeGroups_ObjectIdentity = ObjectIdentity
tnGmplsNeGroups = _TnGmplsNeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 3, 1)
)
_TnGmplsNeCompliances_ObjectIdentity = ObjectIdentity
tnGmplsNeCompliances = _TnGmplsNeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 3, 2)
)

# Managed Objects groups

tnGmplsNeObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 3, 1, 1)
)
tnGmplsNeObjsGroup.setObjects(
    ("TROPIC-GMPLS-NE-MIB", "tnGmplsNeAttributeTotal")
)
if mibBuilder.loadTexts:
    tnGmplsNeObjsGroup.setStatus("current")

tnGmplsNeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 3, 1, 2)
)
tnGmplsNeGroup.setObjects(
      *(("TROPIC-GMPLS-NE-MIB", "tnGmplsNeNodeAddrType"),
        ("TROPIC-GMPLS-NE-MIB", "tnGmplsNeNodeAddr"),
        ("TROPIC-GMPLS-NE-MIB", "tnGmplsNeNotifyAddrType"),
        ("TROPIC-GMPLS-NE-MIB", "tnGmplsNeNotifyAddr"),
        ("TROPIC-GMPLS-NE-MIB", "tnGmplsNeNodeName"),
        ("TROPIC-GMPLS-NE-MIB", "tnGmplsNeDcnOspfArea"),
        ("TROPIC-GMPLS-NE-MIB", "tnGmplsNeRestorationMode"),
        ("TROPIC-GMPLS-NE-MIB", "tnGmplsNeAutomode"),
        ("TROPIC-GMPLS-NE-MIB", "tnGmplsNeActiveNWVersion"),
        ("TROPIC-GMPLS-NE-MIB", "tnGmplsNeInstalledNWVersion"),
        ("TROPIC-GMPLS-NE-MIB", "tnGmplsNeAdminStatus"),
        ("TROPIC-GMPLS-NE-MIB", "tnGmplsNeOperationalState"),
        ("TROPIC-GMPLS-NE-MIB", "tnGmplsNeColocatedNodeAddrType"),
        ("TROPIC-GMPLS-NE-MIB", "tnGmplsNeColocatedNode"),
        ("TROPIC-GMPLS-NE-MIB", "tnGmplsNeRowStatus"))
)
if mibBuilder.loadTexts:
    tnGmplsNeGroup.setStatus("current")

tnGmplsNeSubnodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 3, 1, 3)
)
tnGmplsNeSubnodeGroup.setObjects(
      *(("TROPIC-GMPLS-NE-MIB", "tnGmplsNeSubnodeId"),
        ("TROPIC-GMPLS-NE-MIB", "tnGmplsNeSubnodeAdminStatus"),
        ("TROPIC-GMPLS-NE-MIB", "tnGmplsNeSubnodeRowStatus"))
)
if mibBuilder.loadTexts:
    tnGmplsNeSubnodeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnGmplsNeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1, 4, 3, 2, 1)
)
tnGmplsNeCompliance.setObjects(
      *(("TROPIC-GMPLS-NE-MIB", "tnGmplsNeObjsGroup"),
        ("TROPIC-GMPLS-NE-MIB", "tnGmplsNeGroup"),
        ("TROPIC-GMPLS-NE-MIB", "tnGmplsNeSubnodeGroup"))
)
if mibBuilder.loadTexts:
    tnGmplsNeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-GMPLS-NE-MIB",
    **{"tnGmplsNeMibModule": tnGmplsNeMibModule,
       "tnGmplsNeMIB": tnGmplsNeMIB,
       "tnGmplsNeObjs": tnGmplsNeObjs,
       "tnGmplsNeAttributeTotal": tnGmplsNeAttributeTotal,
       "tnGmplsNeTable": tnGmplsNeTable,
       "tnGmplsNeEntry": tnGmplsNeEntry,
       "tnGmplsNeIndex": tnGmplsNeIndex,
       "tnGmplsNeCPNodeId": tnGmplsNeCPNodeId,
       "tnGmplsNeNodeAddrType": tnGmplsNeNodeAddrType,
       "tnGmplsNeNodeAddr": tnGmplsNeNodeAddr,
       "tnGmplsNeNotifyAddrType": tnGmplsNeNotifyAddrType,
       "tnGmplsNeNotifyAddr": tnGmplsNeNotifyAddr,
       "tnGmplsNeNodeName": tnGmplsNeNodeName,
       "tnGmplsNeDcnOspfArea": tnGmplsNeDcnOspfArea,
       "tnGmplsNeRestorationMode": tnGmplsNeRestorationMode,
       "tnGmplsNeAutomode": tnGmplsNeAutomode,
       "tnGmplsNeActiveNWVersion": tnGmplsNeActiveNWVersion,
       "tnGmplsNeInstalledNWVersion": tnGmplsNeInstalledNWVersion,
       "tnGmplsNeAdminStatus": tnGmplsNeAdminStatus,
       "tnGmplsNeOperationalState": tnGmplsNeOperationalState,
       "tnGmplsNeColocatedNodeAddrType": tnGmplsNeColocatedNodeAddrType,
       "tnGmplsNeColocatedNode": tnGmplsNeColocatedNode,
       "tnGmplsNeRowStatus": tnGmplsNeRowStatus,
       "tnGmplsNeSubnodeTable": tnGmplsNeSubnodeTable,
       "tnGmplsNeSubnodeEntry": tnGmplsNeSubnodeEntry,
       "tnGmplsNeSubnodeIndex": tnGmplsNeSubnodeIndex,
       "tnGmplsNeSubnodeId": tnGmplsNeSubnodeId,
       "tnGmplsNeSubnodeAdminStatus": tnGmplsNeSubnodeAdminStatus,
       "tnGmplsNeSubnodeRowStatus": tnGmplsNeSubnodeRowStatus,
       "tnGmplsNeConf": tnGmplsNeConf,
       "tnGmplsNeGroups": tnGmplsNeGroups,
       "tnGmplsNeObjsGroup": tnGmplsNeObjsGroup,
       "tnGmplsNeGroup": tnGmplsNeGroup,
       "tnGmplsNeSubnodeGroup": tnGmplsNeSubnodeGroup,
       "tnGmplsNeCompliances": tnGmplsNeCompliances,
       "tnGmplsNeCompliance": tnGmplsNeCompliance}
)
