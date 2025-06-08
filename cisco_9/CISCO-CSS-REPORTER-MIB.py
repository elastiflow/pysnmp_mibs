# SNMP MIB module (CISCO-CSS-REPORTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-CSS-REPORTER-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:55:32 2025
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

(ciscoCssReporter,) = mibBuilder.importSymbols(
    "CISCO-APENT-MIB",
    "ciscoCssReporter")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 NotificationType,
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
    "NotificationType",
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

(RowStatus,) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "RowStatus")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCssReporterMIB_ObjectIdentity = ObjectIdentity
ciscoCssReporterMIB = _CiscoCssReporterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1)
)
_CiscoCssReporterMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCssReporterMIBNotifs = _CiscoCssReporterMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 0)
)
_CiscoCssReporterMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCssReporterMIBObjects = _CiscoCssReporterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1)
)
_CcrBaseObjects_ObjectIdentity = ObjectIdentity
ccrBaseObjects = _CcrBaseObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 1)
)
_CcrBaseTable_Object = MibTable
ccrBaseTable = _CcrBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ccrBaseTable.setStatus("mandatory")
_CcrBaseEntry_Object = MibTableRow
ccrBaseEntry = _CcrBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 1, 1, 1)
)
ccrBaseEntry.setIndexNames(
    (0, "CISCO-CSS-REPORTER-MIB", "ccrBaseOID"),
)
if mibBuilder.loadTexts:
    ccrBaseEntry.setStatus("mandatory")
_CcrBaseOID_Type = ObjectIdentifier
_CcrBaseOID_Object = MibTableColumn
ccrBaseOID = _CcrBaseOID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 1, 1, 1, 1),
    _CcrBaseOID_Type()
)
ccrBaseOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccrBaseOID.setStatus("mandatory")


class _CcrBaseName_Type(SnmpAdminString):
    """Custom type ccrBaseName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CcrBaseName_Type.__name__ = "SnmpAdminString"
_CcrBaseName_Object = MibTableColumn
ccrBaseName = _CcrBaseName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 1, 1, 1, 2),
    _CcrBaseName_Type()
)
ccrBaseName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccrBaseName.setStatus("mandatory")


class _CcrBaseType_Type(Integer32):
    """Custom type ccrBaseType based on Integer32"""
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
        *(("none", 1),
          ("criticalPhyAll", 2),
          ("criticalPhyAny", 3),
          ("vridPeering", 4))
    )


_CcrBaseType_Type.__name__ = "Integer32"
_CcrBaseType_Object = MibTableColumn
ccrBaseType = _CcrBaseType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 1, 1, 1, 3),
    _CcrBaseType_Type()
)
ccrBaseType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccrBaseType.setStatus("mandatory")


class _CcrBaseState_Type(Integer32):
    """Custom type ccrBaseState based on Integer32"""
    defaultValue = 1

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
        *(("suspended", 1),
          ("down", 2),
          ("up", 3),
          ("backup", 4),
          ("master", 5))
    )


_CcrBaseState_Type.__name__ = "Integer32"
_CcrBaseState_Object = MibTableColumn
ccrBaseState = _CcrBaseState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 1, 1, 1, 4),
    _CcrBaseState_Type()
)
ccrBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrBaseState.setStatus("mandatory")


class _CcrBaseStateTransitions_Type(Integer32):
    """Custom type ccrBaseStateTransitions based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcrBaseStateTransitions_Type.__name__ = "Integer32"
_CcrBaseStateTransitions_Object = MibTableColumn
ccrBaseStateTransitions = _CcrBaseStateTransitions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 1, 1, 1, 5),
    _CcrBaseStateTransitions_Type()
)
ccrBaseStateTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrBaseStateTransitions.setStatus("mandatory")


class _CcrBaseEnable_Type(Integer32):
    """Custom type ccrBaseEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CcrBaseEnable_Type.__name__ = "Integer32"
_CcrBaseEnable_Object = MibTableColumn
ccrBaseEnable = _CcrBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 1, 1, 1, 6),
    _CcrBaseEnable_Type()
)
ccrBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccrBaseEnable.setStatus("mandatory")


class _CcrBaseTrapEventText_Type(SnmpAdminString):
    """Custom type ccrBaseTrapEventText based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CcrBaseTrapEventText_Type.__name__ = "SnmpAdminString"
_CcrBaseTrapEventText_Object = MibTableColumn
ccrBaseTrapEventText = _CcrBaseTrapEventText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 1, 1, 1, 7),
    _CcrBaseTrapEventText_Type()
)
ccrBaseTrapEventText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrBaseTrapEventText.setStatus("mandatory")


class _CcrBaseZeroButton_Type(Integer32):
    """Custom type ccrBaseZeroButton based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("zeroThisReporterState", 1),
          ("zeroAllReporterState", 2))
    )


_CcrBaseZeroButton_Type.__name__ = "Integer32"
_CcrBaseZeroButton_Object = MibTableColumn
ccrBaseZeroButton = _CcrBaseZeroButton_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 1, 1, 1, 8),
    _CcrBaseZeroButton_Type()
)
ccrBaseZeroButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccrBaseZeroButton.setStatus("mandatory")
_CcrBaseStatus_Type = RowStatus
_CcrBaseStatus_Object = MibTableColumn
ccrBaseStatus = _CcrBaseStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 1, 1, 1, 9),
    _CcrBaseStatus_Type()
)
ccrBaseStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccrBaseStatus.setStatus("mandatory")
_CcrIfObjects_ObjectIdentity = ObjectIdentity
ccrIfObjects = _CcrIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 2)
)
_CcrIfTable_Object = MibTable
ccrIfTable = _CcrIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ccrIfTable.setStatus("mandatory")
_CcrIfEntry_Object = MibTableRow
ccrIfEntry = _CcrIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 2, 1, 1)
)
ccrIfEntry.setIndexNames(
    (0, "CISCO-CSS-REPORTER-MIB", "ccrIfOID"),
)
if mibBuilder.loadTexts:
    ccrIfEntry.setStatus("mandatory")
_CcrIfOID_Type = ObjectIdentifier
_CcrIfOID_Object = MibTableColumn
ccrIfOID = _CcrIfOID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 2, 1, 1, 1),
    _CcrIfOID_Type()
)
ccrIfOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccrIfOID.setStatus("mandatory")


class _CcrIfName_Type(SnmpAdminString):
    """Custom type ccrIfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CcrIfName_Type.__name__ = "SnmpAdminString"
_CcrIfName_Object = MibTableColumn
ccrIfName = _CcrIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 2, 1, 1, 2),
    _CcrIfName_Type()
)
ccrIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccrIfName.setStatus("mandatory")


class _CcrIfIndex_Type(Integer32):
    """Custom type ccrIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CcrIfIndex_Type.__name__ = "Integer32"
_CcrIfIndex_Object = MibTableColumn
ccrIfIndex = _CcrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 2, 1, 1, 3),
    _CcrIfIndex_Type()
)
ccrIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccrIfIndex.setStatus("mandatory")


class _CcrIfDescr_Type(SnmpAdminString):
    """Custom type ccrIfDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CcrIfDescr_Type.__name__ = "SnmpAdminString"
_CcrIfDescr_Object = MibTableColumn
ccrIfDescr = _CcrIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 2, 1, 1, 4),
    _CcrIfDescr_Type()
)
ccrIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrIfDescr.setStatus("mandatory")


class _CcrIfState_Type(Integer32):
    """Custom type ccrIfState based on Integer32"""
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


_CcrIfState_Type.__name__ = "Integer32"
_CcrIfState_Object = MibTableColumn
ccrIfState = _CcrIfState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 2, 1, 1, 5),
    _CcrIfState_Type()
)
ccrIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrIfState.setStatus("mandatory")


class _CcrIfStateTransitions_Type(Integer32):
    """Custom type ccrIfStateTransitions based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcrIfStateTransitions_Type.__name__ = "Integer32"
_CcrIfStateTransitions_Object = MibTableColumn
ccrIfStateTransitions = _CcrIfStateTransitions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 2, 1, 1, 6),
    _CcrIfStateTransitions_Type()
)
ccrIfStateTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrIfStateTransitions.setStatus("mandatory")
_CcrIfStatus_Type = RowStatus
_CcrIfStatus_Object = MibTableColumn
ccrIfStatus = _CcrIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 2, 1, 1, 7),
    _CcrIfStatus_Type()
)
ccrIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccrIfStatus.setStatus("mandatory")
_CcrVridObjects_ObjectIdentity = ObjectIdentity
ccrVridObjects = _CcrVridObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 3)
)
_CcrVridTable_Object = MibTable
ccrVridTable = _CcrVridTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ccrVridTable.setStatus("mandatory")
_CcrVridEntry_Object = MibTableRow
ccrVridEntry = _CcrVridEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 3, 1, 1)
)
ccrVridEntry.setIndexNames(
    (0, "CISCO-CSS-REPORTER-MIB", "ccrVridOID"),
)
if mibBuilder.loadTexts:
    ccrVridEntry.setStatus("mandatory")
_CcrVridOID_Type = ObjectIdentifier
_CcrVridOID_Object = MibTableColumn
ccrVridOID = _CcrVridOID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 3, 1, 1, 1),
    _CcrVridOID_Type()
)
ccrVridOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccrVridOID.setStatus("mandatory")


class _CcrVridName_Type(SnmpAdminString):
    """Custom type ccrVridName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CcrVridName_Type.__name__ = "SnmpAdminString"
_CcrVridName_Object = MibTableColumn
ccrVridName = _CcrVridName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 3, 1, 1, 2),
    _CcrVridName_Type()
)
ccrVridName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccrVridName.setStatus("mandatory")


class _CcrVridCircuitIpAddrType_Type(InetAddressType):
    """Custom type ccrVridCircuitIpAddrType based on InetAddressType"""
    defaultValue = 1


_CcrVridCircuitIpAddrType_Type.__name__ = "InetAddressType"
_CcrVridCircuitIpAddrType_Object = MibTableColumn
ccrVridCircuitIpAddrType = _CcrVridCircuitIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 3, 1, 1, 3),
    _CcrVridCircuitIpAddrType_Type()
)
ccrVridCircuitIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccrVridCircuitIpAddrType.setStatus("mandatory")
_CcrVridCircuitIpAddr_Type = InetAddress
_CcrVridCircuitIpAddr_Object = MibTableColumn
ccrVridCircuitIpAddr = _CcrVridCircuitIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 3, 1, 1, 4),
    _CcrVridCircuitIpAddr_Type()
)
ccrVridCircuitIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccrVridCircuitIpAddr.setStatus("mandatory")


class _CcrVridRouterId_Type(Integer32):
    """Custom type ccrVridRouterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CcrVridRouterId_Type.__name__ = "Integer32"
_CcrVridRouterId_Object = MibTableColumn
ccrVridRouterId = _CcrVridRouterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 3, 1, 1, 5),
    _CcrVridRouterId_Type()
)
ccrVridRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrVridRouterId.setStatus("mandatory")


class _CcrVridState_Type(Integer32):
    """Custom type ccrVridState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("backup", 4),
          ("master", 5))
    )


_CcrVridState_Type.__name__ = "Integer32"
_CcrVridState_Object = MibTableColumn
ccrVridState = _CcrVridState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 3, 1, 1, 6),
    _CcrVridState_Type()
)
ccrVridState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrVridState.setStatus("mandatory")


class _CcrVridStateTransitions_Type(Integer32):
    """Custom type ccrVridStateTransitions based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcrVridStateTransitions_Type.__name__ = "Integer32"
_CcrVridStateTransitions_Object = MibTableColumn
ccrVridStateTransitions = _CcrVridStateTransitions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 3, 1, 1, 7),
    _CcrVridStateTransitions_Type()
)
ccrVridStateTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrVridStateTransitions.setStatus("mandatory")
_CcrVridStatus_Type = RowStatus
_CcrVridStatus_Object = MibTableColumn
ccrVridStatus = _CcrVridStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 1, 3, 1, 1, 8),
    _CcrVridStatus_Type()
)
ccrVridStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccrVridStatus.setStatus("mandatory")
_CiscoCssReporterMIBConform_ObjectIdentity = ObjectIdentity
ciscoCssReporterMIBConform = _CiscoCssReporterMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 2)
)
_CiscoCssReporterMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCssReporterMIBCompliances = _CiscoCssReporterMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 2, 1)
)
_CiscoCssReporterMIBCompliance_ObjectIdentity = ObjectIdentity
ciscoCssReporterMIBCompliance = _CiscoCssReporterMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 2, 1, 1)
)
_CiscoCssReporterMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCssReporterMIBGroups = _CiscoCssReporterMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 2, 2)
)
_CiscoCssReporterMIBGroup_ObjectIdentity = ObjectIdentity
ciscoCssReporterMIBGroup = _CiscoCssReporterMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 2, 2, 1)
)
_CiscoCssReporterMIBNotif_ObjectIdentity = ObjectIdentity
ciscoCssReporterMIBNotif = _CiscoCssReporterMIBNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 2, 2, 2)
)

# Managed Objects groups


# Notification objects

ciscoCssReporterTransitionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 68, 1, 0, 1)
)
ciscoCssReporterTransitionTrap.setObjects(
      *(("CISCO-CSS-REPORTER-MIB", "ccrBaseTrapEventText"),
        ("CISCO-CSS-REPORTER-MIB", "ccrBaseName"),
        ("CISCO-CSS-REPORTER-MIB", "ccrBaseState"))
)
if mibBuilder.loadTexts:
    ciscoCssReporterTransitionTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CSS-REPORTER-MIB",
    **{"ciscoCssReporterMIB": ciscoCssReporterMIB,
       "ciscoCssReporterMIBNotifs": ciscoCssReporterMIBNotifs,
       "ciscoCssReporterTransitionTrap": ciscoCssReporterTransitionTrap,
       "ciscoCssReporterMIBObjects": ciscoCssReporterMIBObjects,
       "ccrBaseObjects": ccrBaseObjects,
       "ccrBaseTable": ccrBaseTable,
       "ccrBaseEntry": ccrBaseEntry,
       "ccrBaseOID": ccrBaseOID,
       "ccrBaseName": ccrBaseName,
       "ccrBaseType": ccrBaseType,
       "ccrBaseState": ccrBaseState,
       "ccrBaseStateTransitions": ccrBaseStateTransitions,
       "ccrBaseEnable": ccrBaseEnable,
       "ccrBaseTrapEventText": ccrBaseTrapEventText,
       "ccrBaseZeroButton": ccrBaseZeroButton,
       "ccrBaseStatus": ccrBaseStatus,
       "ccrIfObjects": ccrIfObjects,
       "ccrIfTable": ccrIfTable,
       "ccrIfEntry": ccrIfEntry,
       "ccrIfOID": ccrIfOID,
       "ccrIfName": ccrIfName,
       "ccrIfIndex": ccrIfIndex,
       "ccrIfDescr": ccrIfDescr,
       "ccrIfState": ccrIfState,
       "ccrIfStateTransitions": ccrIfStateTransitions,
       "ccrIfStatus": ccrIfStatus,
       "ccrVridObjects": ccrVridObjects,
       "ccrVridTable": ccrVridTable,
       "ccrVridEntry": ccrVridEntry,
       "ccrVridOID": ccrVridOID,
       "ccrVridName": ccrVridName,
       "ccrVridCircuitIpAddrType": ccrVridCircuitIpAddrType,
       "ccrVridCircuitIpAddr": ccrVridCircuitIpAddr,
       "ccrVridRouterId": ccrVridRouterId,
       "ccrVridState": ccrVridState,
       "ccrVridStateTransitions": ccrVridStateTransitions,
       "ccrVridStatus": ccrVridStatus,
       "ciscoCssReporterMIBConform": ciscoCssReporterMIBConform,
       "ciscoCssReporterMIBCompliances": ciscoCssReporterMIBCompliances,
       "ciscoCssReporterMIBCompliance": ciscoCssReporterMIBCompliance,
       "ciscoCssReporterMIBGroups": ciscoCssReporterMIBGroups,
       "ciscoCssReporterMIBGroup": ciscoCssReporterMIBGroup,
       "ciscoCssReporterMIBNotif": ciscoCssReporterMIBNotif}
)
