# SNMP MIB module (SNMP-REPEATER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/SNMP-REPEATER-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 15:05:38 2025
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

(OwnerString,) = mibBuilder.importSymbols(
    "IF-MIB",
    "OwnerString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp")


# MODULE-IDENTITY

snmpRptrMod = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 22, 5)
)
if mibBuilder.loadTexts:
    snmpRptrMod.setRevisions(
        ("1993-09-01 00:00",
         "1992-10-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class OptMacAddr(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 6),
    )



# MIB Managed Objects in the order of their OIDs

_SnmpDot3RptrMgt_ObjectIdentity = ObjectIdentity
snmpDot3RptrMgt = _SnmpDot3RptrMgt_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22)
)
_RptrBasicPackage_ObjectIdentity = ObjectIdentity
rptrBasicPackage = _RptrBasicPackage_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1)
)
_RptrRptrInfo_ObjectIdentity = ObjectIdentity
rptrRptrInfo = _RptrRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1, 1)
)


class _RptrGroupCapacity_Type(Integer32):
    """Custom type rptrGroupCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RptrGroupCapacity_Type.__name__ = "Integer32"
_RptrGroupCapacity_Object = MibScalar
rptrGroupCapacity = _RptrGroupCapacity_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 1, 1),
    _RptrGroupCapacity_Type()
)
rptrGroupCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupCapacity.setStatus("deprecated")


class _RptrOperStatus_Type(Integer32):
    """Custom type rptrOperStatus based on Integer32"""
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
        *(("other", 1),
          ("ok", 2),
          ("rptrFailure", 3),
          ("groupFailure", 4),
          ("portFailure", 5),
          ("generalFailure", 6))
    )


_RptrOperStatus_Type.__name__ = "Integer32"
_RptrOperStatus_Object = MibScalar
rptrOperStatus = _RptrOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 1, 2),
    _RptrOperStatus_Type()
)
rptrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrOperStatus.setStatus("deprecated")


class _RptrHealthText_Type(DisplayString):
    """Custom type rptrHealthText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RptrHealthText_Type.__name__ = "DisplayString"
_RptrHealthText_Object = MibScalar
rptrHealthText = _RptrHealthText_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 1, 3),
    _RptrHealthText_Type()
)
rptrHealthText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrHealthText.setStatus("deprecated")


class _RptrReset_Type(Integer32):
    """Custom type rptrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_RptrReset_Type.__name__ = "Integer32"
_RptrReset_Object = MibScalar
rptrReset = _RptrReset_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 1, 4),
    _RptrReset_Type()
)
rptrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrReset.setStatus("deprecated")


class _RptrNonDisruptTest_Type(Integer32):
    """Custom type rptrNonDisruptTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSelfTest", 1),
          ("selfTest", 2))
    )


_RptrNonDisruptTest_Type.__name__ = "Integer32"
_RptrNonDisruptTest_Object = MibScalar
rptrNonDisruptTest = _RptrNonDisruptTest_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 1, 5),
    _RptrNonDisruptTest_Type()
)
rptrNonDisruptTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrNonDisruptTest.setStatus("deprecated")
_RptrTotalPartitionedPorts_Type = Gauge32
_RptrTotalPartitionedPorts_Object = MibScalar
rptrTotalPartitionedPorts = _RptrTotalPartitionedPorts_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 1, 6),
    _RptrTotalPartitionedPorts_Type()
)
rptrTotalPartitionedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrTotalPartitionedPorts.setStatus("deprecated")
_RptrGroupInfo_ObjectIdentity = ObjectIdentity
rptrGroupInfo = _RptrGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1, 2)
)
_RptrGroupTable_Object = MibTable
rptrGroupTable = _RptrGroupTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rptrGroupTable.setStatus("current")
_RptrGroupEntry_Object = MibTableRow
rptrGroupEntry = _RptrGroupEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1)
)
rptrGroupEntry.setIndexNames(
    (0, "SNMP-REPEATER-MIB", "rptrGroupIndex"),
)
if mibBuilder.loadTexts:
    rptrGroupEntry.setStatus("current")


class _RptrGroupIndex_Type(Integer32):
    """Custom type rptrGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RptrGroupIndex_Type.__name__ = "Integer32"
_RptrGroupIndex_Object = MibTableColumn
rptrGroupIndex = _RptrGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 1),
    _RptrGroupIndex_Type()
)
rptrGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupIndex.setStatus("current")


class _RptrGroupDescr_Type(DisplayString):
    """Custom type rptrGroupDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RptrGroupDescr_Type.__name__ = "DisplayString"
_RptrGroupDescr_Object = MibTableColumn
rptrGroupDescr = _RptrGroupDescr_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 2),
    _RptrGroupDescr_Type()
)
rptrGroupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupDescr.setStatus("deprecated")
_RptrGroupObjectID_Type = ObjectIdentifier
_RptrGroupObjectID_Object = MibTableColumn
rptrGroupObjectID = _RptrGroupObjectID_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 3),
    _RptrGroupObjectID_Type()
)
rptrGroupObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupObjectID.setStatus("current")


class _RptrGroupOperStatus_Type(Integer32):
    """Custom type rptrGroupOperStatus based on Integer32"""
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
        *(("other", 1),
          ("operational", 2),
          ("malfunctioning", 3),
          ("notPresent", 4),
          ("underTest", 5),
          ("resetInProgress", 6))
    )


_RptrGroupOperStatus_Type.__name__ = "Integer32"
_RptrGroupOperStatus_Object = MibTableColumn
rptrGroupOperStatus = _RptrGroupOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 4),
    _RptrGroupOperStatus_Type()
)
rptrGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupOperStatus.setStatus("current")
_RptrGroupLastOperStatusChange_Type = TimeTicks
_RptrGroupLastOperStatusChange_Object = MibTableColumn
rptrGroupLastOperStatusChange = _RptrGroupLastOperStatusChange_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 5),
    _RptrGroupLastOperStatusChange_Type()
)
rptrGroupLastOperStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupLastOperStatusChange.setStatus("deprecated")


class _RptrGroupPortCapacity_Type(Integer32):
    """Custom type rptrGroupPortCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RptrGroupPortCapacity_Type.__name__ = "Integer32"
_RptrGroupPortCapacity_Object = MibTableColumn
rptrGroupPortCapacity = _RptrGroupPortCapacity_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 6),
    _RptrGroupPortCapacity_Type()
)
rptrGroupPortCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupPortCapacity.setStatus("current")
_RptrPortInfo_ObjectIdentity = ObjectIdentity
rptrPortInfo = _RptrPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1, 3)
)
_RptrPortTable_Object = MibTable
rptrPortTable = _RptrPortTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rptrPortTable.setStatus("current")
_RptrPortEntry_Object = MibTableRow
rptrPortEntry = _RptrPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1)
)
rptrPortEntry.setIndexNames(
    (0, "SNMP-REPEATER-MIB", "rptrPortGroupIndex"),
    (0, "SNMP-REPEATER-MIB", "rptrPortIndex"),
)
if mibBuilder.loadTexts:
    rptrPortEntry.setStatus("current")


class _RptrPortGroupIndex_Type(Integer32):
    """Custom type rptrPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RptrPortGroupIndex_Type.__name__ = "Integer32"
_RptrPortGroupIndex_Object = MibTableColumn
rptrPortGroupIndex = _RptrPortGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 1),
    _RptrPortGroupIndex_Type()
)
rptrPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGroupIndex.setStatus("current")


class _RptrPortIndex_Type(Integer32):
    """Custom type rptrPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RptrPortIndex_Type.__name__ = "Integer32"
_RptrPortIndex_Object = MibTableColumn
rptrPortIndex = _RptrPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 2),
    _RptrPortIndex_Type()
)
rptrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortIndex.setStatus("current")


class _RptrPortAdminStatus_Type(Integer32):
    """Custom type rptrPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RptrPortAdminStatus_Type.__name__ = "Integer32"
_RptrPortAdminStatus_Object = MibTableColumn
rptrPortAdminStatus = _RptrPortAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 3),
    _RptrPortAdminStatus_Type()
)
rptrPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortAdminStatus.setStatus("current")


class _RptrPortAutoPartitionState_Type(Integer32):
    """Custom type rptrPortAutoPartitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAutoPartitioned", 1),
          ("autoPartitioned", 2))
    )


_RptrPortAutoPartitionState_Type.__name__ = "Integer32"
_RptrPortAutoPartitionState_Object = MibTableColumn
rptrPortAutoPartitionState = _RptrPortAutoPartitionState_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 4),
    _RptrPortAutoPartitionState_Type()
)
rptrPortAutoPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortAutoPartitionState.setStatus("current")


class _RptrPortOperStatus_Type(Integer32):
    """Custom type rptrPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("operational", 1),
          ("notOperational", 2),
          ("notPresent", 3))
    )


_RptrPortOperStatus_Type.__name__ = "Integer32"
_RptrPortOperStatus_Object = MibTableColumn
rptrPortOperStatus = _RptrPortOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 5),
    _RptrPortOperStatus_Type()
)
rptrPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortOperStatus.setStatus("current")


class _RptrPortRptrId_Type(Integer32):
    """Custom type rptrPortRptrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RptrPortRptrId_Type.__name__ = "Integer32"
_RptrPortRptrId_Object = MibTableColumn
rptrPortRptrId = _RptrPortRptrId_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 6),
    _RptrPortRptrId_Type()
)
rptrPortRptrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortRptrId.setStatus("current")
_RptrAllRptrInfo_ObjectIdentity = ObjectIdentity
rptrAllRptrInfo = _RptrAllRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1, 4)
)
_RptrInfoTable_Object = MibTable
rptrInfoTable = _RptrInfoTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 4, 1)
)
if mibBuilder.loadTexts:
    rptrInfoTable.setStatus("current")
_RptrInfoEntry_Object = MibTableRow
rptrInfoEntry = _RptrInfoEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 4, 1, 1)
)
rptrInfoEntry.setIndexNames(
    (0, "SNMP-REPEATER-MIB", "rptrInfoId"),
)
if mibBuilder.loadTexts:
    rptrInfoEntry.setStatus("current")


class _RptrInfoId_Type(Integer32):
    """Custom type rptrInfoId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RptrInfoId_Type.__name__ = "Integer32"
_RptrInfoId_Object = MibTableColumn
rptrInfoId = _RptrInfoId_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 4, 1, 1, 1),
    _RptrInfoId_Type()
)
rptrInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrInfoId.setStatus("current")


class _RptrInfoRptrType_Type(Integer32):
    """Custom type rptrInfoRptrType based on Integer32"""
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
        *(("other", 1),
          ("tenMb", 2),
          ("onehundredMbClassI", 3),
          ("onehundredMbClassII", 4))
    )


_RptrInfoRptrType_Type.__name__ = "Integer32"
_RptrInfoRptrType_Object = MibTableColumn
rptrInfoRptrType = _RptrInfoRptrType_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 4, 1, 1, 2),
    _RptrInfoRptrType_Type()
)
rptrInfoRptrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrInfoRptrType.setStatus("current")


class _RptrInfoOperStatus_Type(Integer32):
    """Custom type rptrInfoOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ok", 2),
          ("failure", 3))
    )


_RptrInfoOperStatus_Type.__name__ = "Integer32"
_RptrInfoOperStatus_Object = MibTableColumn
rptrInfoOperStatus = _RptrInfoOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 4, 1, 1, 3),
    _RptrInfoOperStatus_Type()
)
rptrInfoOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrInfoOperStatus.setStatus("current")


class _RptrInfoReset_Type(Integer32):
    """Custom type rptrInfoReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_RptrInfoReset_Type.__name__ = "Integer32"
_RptrInfoReset_Object = MibTableColumn
rptrInfoReset = _RptrInfoReset_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 4, 1, 1, 4),
    _RptrInfoReset_Type()
)
rptrInfoReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrInfoReset.setStatus("current")
_RptrInfoPartitionedPorts_Type = Gauge32
_RptrInfoPartitionedPorts_Object = MibTableColumn
rptrInfoPartitionedPorts = _RptrInfoPartitionedPorts_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 4, 1, 1, 5),
    _RptrInfoPartitionedPorts_Type()
)
rptrInfoPartitionedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrInfoPartitionedPorts.setStatus("current")
_RptrInfoLastChange_Type = TimeStamp
_RptrInfoLastChange_Object = MibTableColumn
rptrInfoLastChange = _RptrInfoLastChange_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 4, 1, 1, 6),
    _RptrInfoLastChange_Type()
)
rptrInfoLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrInfoLastChange.setStatus("current")
_RptrMonitorPackage_ObjectIdentity = ObjectIdentity
rptrMonitorPackage = _RptrMonitorPackage_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 2)
)
_RptrMonitorRptrInfo_ObjectIdentity = ObjectIdentity
rptrMonitorRptrInfo = _RptrMonitorRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 2, 1)
)
_RptrMonitorTransmitCollisions_Type = Counter32
_RptrMonitorTransmitCollisions_Object = MibScalar
rptrMonitorTransmitCollisions = _RptrMonitorTransmitCollisions_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 1, 1),
    _RptrMonitorTransmitCollisions_Type()
)
rptrMonitorTransmitCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorTransmitCollisions.setStatus("deprecated")
_RptrMonitorGroupInfo_ObjectIdentity = ObjectIdentity
rptrMonitorGroupInfo = _RptrMonitorGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 2, 2)
)
_RptrMonitorGroupTable_Object = MibTable
rptrMonitorGroupTable = _RptrMonitorGroupTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rptrMonitorGroupTable.setStatus("deprecated")
_RptrMonitorGroupEntry_Object = MibTableRow
rptrMonitorGroupEntry = _RptrMonitorGroupEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1)
)
rptrMonitorGroupEntry.setIndexNames(
    (0, "SNMP-REPEATER-MIB", "rptrMonitorGroupIndex"),
)
if mibBuilder.loadTexts:
    rptrMonitorGroupEntry.setStatus("deprecated")


class _RptrMonitorGroupIndex_Type(Integer32):
    """Custom type rptrMonitorGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RptrMonitorGroupIndex_Type.__name__ = "Integer32"
_RptrMonitorGroupIndex_Object = MibTableColumn
rptrMonitorGroupIndex = _RptrMonitorGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1, 1),
    _RptrMonitorGroupIndex_Type()
)
rptrMonitorGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorGroupIndex.setStatus("deprecated")
_RptrMonitorGroupTotalFrames_Type = Counter32
_RptrMonitorGroupTotalFrames_Object = MibTableColumn
rptrMonitorGroupTotalFrames = _RptrMonitorGroupTotalFrames_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1, 2),
    _RptrMonitorGroupTotalFrames_Type()
)
rptrMonitorGroupTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorGroupTotalFrames.setStatus("deprecated")
_RptrMonitorGroupTotalOctets_Type = Counter32
_RptrMonitorGroupTotalOctets_Object = MibTableColumn
rptrMonitorGroupTotalOctets = _RptrMonitorGroupTotalOctets_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1, 3),
    _RptrMonitorGroupTotalOctets_Type()
)
rptrMonitorGroupTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorGroupTotalOctets.setStatus("deprecated")
_RptrMonitorGroupTotalErrors_Type = Counter32
_RptrMonitorGroupTotalErrors_Object = MibTableColumn
rptrMonitorGroupTotalErrors = _RptrMonitorGroupTotalErrors_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1, 4),
    _RptrMonitorGroupTotalErrors_Type()
)
rptrMonitorGroupTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorGroupTotalErrors.setStatus("deprecated")
_RptrMonitorPortInfo_ObjectIdentity = ObjectIdentity
rptrMonitorPortInfo = _RptrMonitorPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 2, 3)
)
_RptrMonitorPortTable_Object = MibTable
rptrMonitorPortTable = _RptrMonitorPortTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1)
)
if mibBuilder.loadTexts:
    rptrMonitorPortTable.setStatus("current")
_RptrMonitorPortEntry_Object = MibTableRow
rptrMonitorPortEntry = _RptrMonitorPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1)
)
rptrMonitorPortEntry.setIndexNames(
    (0, "SNMP-REPEATER-MIB", "rptrMonitorPortGroupIndex"),
    (0, "SNMP-REPEATER-MIB", "rptrMonitorPortIndex"),
)
if mibBuilder.loadTexts:
    rptrMonitorPortEntry.setStatus("current")


class _RptrMonitorPortGroupIndex_Type(Integer32):
    """Custom type rptrMonitorPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RptrMonitorPortGroupIndex_Type.__name__ = "Integer32"
_RptrMonitorPortGroupIndex_Object = MibTableColumn
rptrMonitorPortGroupIndex = _RptrMonitorPortGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 1),
    _RptrMonitorPortGroupIndex_Type()
)
rptrMonitorPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortGroupIndex.setStatus("current")


class _RptrMonitorPortIndex_Type(Integer32):
    """Custom type rptrMonitorPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RptrMonitorPortIndex_Type.__name__ = "Integer32"
_RptrMonitorPortIndex_Object = MibTableColumn
rptrMonitorPortIndex = _RptrMonitorPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 2),
    _RptrMonitorPortIndex_Type()
)
rptrMonitorPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortIndex.setStatus("current")
_RptrMonitorPortReadableFrames_Type = Counter32
_RptrMonitorPortReadableFrames_Object = MibTableColumn
rptrMonitorPortReadableFrames = _RptrMonitorPortReadableFrames_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 3),
    _RptrMonitorPortReadableFrames_Type()
)
rptrMonitorPortReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortReadableFrames.setStatus("current")
_RptrMonitorPortReadableOctets_Type = Counter32
_RptrMonitorPortReadableOctets_Object = MibTableColumn
rptrMonitorPortReadableOctets = _RptrMonitorPortReadableOctets_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 4),
    _RptrMonitorPortReadableOctets_Type()
)
rptrMonitorPortReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortReadableOctets.setStatus("current")
_RptrMonitorPortFCSErrors_Type = Counter32
_RptrMonitorPortFCSErrors_Object = MibTableColumn
rptrMonitorPortFCSErrors = _RptrMonitorPortFCSErrors_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 5),
    _RptrMonitorPortFCSErrors_Type()
)
rptrMonitorPortFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortFCSErrors.setStatus("current")
_RptrMonitorPortAlignmentErrors_Type = Counter32
_RptrMonitorPortAlignmentErrors_Object = MibTableColumn
rptrMonitorPortAlignmentErrors = _RptrMonitorPortAlignmentErrors_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 6),
    _RptrMonitorPortAlignmentErrors_Type()
)
rptrMonitorPortAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortAlignmentErrors.setStatus("current")
_RptrMonitorPortFrameTooLongs_Type = Counter32
_RptrMonitorPortFrameTooLongs_Object = MibTableColumn
rptrMonitorPortFrameTooLongs = _RptrMonitorPortFrameTooLongs_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 7),
    _RptrMonitorPortFrameTooLongs_Type()
)
rptrMonitorPortFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortFrameTooLongs.setStatus("current")
_RptrMonitorPortShortEvents_Type = Counter32
_RptrMonitorPortShortEvents_Object = MibTableColumn
rptrMonitorPortShortEvents = _RptrMonitorPortShortEvents_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 8),
    _RptrMonitorPortShortEvents_Type()
)
rptrMonitorPortShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortShortEvents.setStatus("current")
_RptrMonitorPortRunts_Type = Counter32
_RptrMonitorPortRunts_Object = MibTableColumn
rptrMonitorPortRunts = _RptrMonitorPortRunts_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 9),
    _RptrMonitorPortRunts_Type()
)
rptrMonitorPortRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortRunts.setStatus("current")
_RptrMonitorPortCollisions_Type = Counter32
_RptrMonitorPortCollisions_Object = MibTableColumn
rptrMonitorPortCollisions = _RptrMonitorPortCollisions_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 10),
    _RptrMonitorPortCollisions_Type()
)
rptrMonitorPortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortCollisions.setStatus("current")
_RptrMonitorPortLateEvents_Type = Counter32
_RptrMonitorPortLateEvents_Object = MibTableColumn
rptrMonitorPortLateEvents = _RptrMonitorPortLateEvents_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 11),
    _RptrMonitorPortLateEvents_Type()
)
rptrMonitorPortLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortLateEvents.setStatus("current")
_RptrMonitorPortVeryLongEvents_Type = Counter32
_RptrMonitorPortVeryLongEvents_Object = MibTableColumn
rptrMonitorPortVeryLongEvents = _RptrMonitorPortVeryLongEvents_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 12),
    _RptrMonitorPortVeryLongEvents_Type()
)
rptrMonitorPortVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortVeryLongEvents.setStatus("current")
_RptrMonitorPortDataRateMismatches_Type = Counter32
_RptrMonitorPortDataRateMismatches_Object = MibTableColumn
rptrMonitorPortDataRateMismatches = _RptrMonitorPortDataRateMismatches_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 13),
    _RptrMonitorPortDataRateMismatches_Type()
)
rptrMonitorPortDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortDataRateMismatches.setStatus("current")
_RptrMonitorPortAutoPartitions_Type = Counter32
_RptrMonitorPortAutoPartitions_Object = MibTableColumn
rptrMonitorPortAutoPartitions = _RptrMonitorPortAutoPartitions_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 14),
    _RptrMonitorPortAutoPartitions_Type()
)
rptrMonitorPortAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortAutoPartitions.setStatus("current")
_RptrMonitorPortTotalErrors_Type = Counter32
_RptrMonitorPortTotalErrors_Object = MibTableColumn
rptrMonitorPortTotalErrors = _RptrMonitorPortTotalErrors_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 15),
    _RptrMonitorPortTotalErrors_Type()
)
rptrMonitorPortTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortTotalErrors.setStatus("current")
_RptrMonitorPortLastChange_Type = TimeStamp
_RptrMonitorPortLastChange_Object = MibTableColumn
rptrMonitorPortLastChange = _RptrMonitorPortLastChange_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 16),
    _RptrMonitorPortLastChange_Type()
)
rptrMonitorPortLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortLastChange.setStatus("current")
_RptrMonitor100PortTable_Object = MibTable
rptrMonitor100PortTable = _RptrMonitor100PortTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 2)
)
if mibBuilder.loadTexts:
    rptrMonitor100PortTable.setStatus("current")
_RptrMonitor100PortEntry_Object = MibTableRow
rptrMonitor100PortEntry = _RptrMonitor100PortEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 2, 1)
)
rptrMonitor100PortEntry.setIndexNames(
    (0, "SNMP-REPEATER-MIB", "rptrMonitorPortGroupIndex"),
    (0, "SNMP-REPEATER-MIB", "rptrMonitorPortIndex"),
)
if mibBuilder.loadTexts:
    rptrMonitor100PortEntry.setStatus("current")
_RptrMonitorPortIsolates_Type = Counter32
_RptrMonitorPortIsolates_Object = MibTableColumn
rptrMonitorPortIsolates = _RptrMonitorPortIsolates_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 2, 1, 1),
    _RptrMonitorPortIsolates_Type()
)
rptrMonitorPortIsolates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortIsolates.setStatus("current")
_RptrMonitorPortSymbolErrors_Type = Counter32
_RptrMonitorPortSymbolErrors_Object = MibTableColumn
rptrMonitorPortSymbolErrors = _RptrMonitorPortSymbolErrors_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 2, 1, 2),
    _RptrMonitorPortSymbolErrors_Type()
)
rptrMonitorPortSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortSymbolErrors.setStatus("current")
_RptrMonitorPortUpper32Octets_Type = Counter32
_RptrMonitorPortUpper32Octets_Object = MibTableColumn
rptrMonitorPortUpper32Octets = _RptrMonitorPortUpper32Octets_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 2, 1, 3),
    _RptrMonitorPortUpper32Octets_Type()
)
rptrMonitorPortUpper32Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortUpper32Octets.setStatus("current")
_RptrMonitorPortHCReadableOctets_Type = Counter64
_RptrMonitorPortHCReadableOctets_Object = MibTableColumn
rptrMonitorPortHCReadableOctets = _RptrMonitorPortHCReadableOctets_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 2, 1, 4),
    _RptrMonitorPortHCReadableOctets_Type()
)
rptrMonitorPortHCReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortHCReadableOctets.setStatus("current")
_RptrMonitorAllRptrInfo_ObjectIdentity = ObjectIdentity
rptrMonitorAllRptrInfo = _RptrMonitorAllRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 2, 4)
)
_RptrMonTable_Object = MibTable
rptrMonTable = _RptrMonTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 4, 1)
)
if mibBuilder.loadTexts:
    rptrMonTable.setStatus("current")
_RptrMonEntry_Object = MibTableRow
rptrMonEntry = _RptrMonEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 4, 1, 1)
)
rptrMonEntry.setIndexNames(
    (0, "SNMP-REPEATER-MIB", "rptrInfoId"),
)
if mibBuilder.loadTexts:
    rptrMonEntry.setStatus("current")
_RptrMonTxCollisions_Type = Counter32
_RptrMonTxCollisions_Object = MibTableColumn
rptrMonTxCollisions = _RptrMonTxCollisions_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 4, 1, 1, 1),
    _RptrMonTxCollisions_Type()
)
rptrMonTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonTxCollisions.setStatus("current")
_RptrMonTotalFrames_Type = Counter32
_RptrMonTotalFrames_Object = MibTableColumn
rptrMonTotalFrames = _RptrMonTotalFrames_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 4, 1, 1, 3),
    _RptrMonTotalFrames_Type()
)
rptrMonTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonTotalFrames.setStatus("current")
_RptrMonTotalErrors_Type = Counter32
_RptrMonTotalErrors_Object = MibTableColumn
rptrMonTotalErrors = _RptrMonTotalErrors_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 4, 1, 1, 4),
    _RptrMonTotalErrors_Type()
)
rptrMonTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonTotalErrors.setStatus("current")
_RptrMonTotalOctets_Type = Counter32
_RptrMonTotalOctets_Object = MibTableColumn
rptrMonTotalOctets = _RptrMonTotalOctets_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 4, 1, 1, 5),
    _RptrMonTotalOctets_Type()
)
rptrMonTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonTotalOctets.setStatus("current")
_RptrMon100Table_Object = MibTable
rptrMon100Table = _RptrMon100Table_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 4, 2)
)
if mibBuilder.loadTexts:
    rptrMon100Table.setStatus("current")
_RptrMon100Entry_Object = MibTableRow
rptrMon100Entry = _RptrMon100Entry_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 4, 2, 1)
)
rptrMon100Entry.setIndexNames(
    (0, "SNMP-REPEATER-MIB", "rptrInfoId"),
)
if mibBuilder.loadTexts:
    rptrMon100Entry.setStatus("current")
_RptrMonUpper32TotalOctets_Type = Counter32
_RptrMonUpper32TotalOctets_Object = MibTableColumn
rptrMonUpper32TotalOctets = _RptrMonUpper32TotalOctets_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 4, 2, 1, 1),
    _RptrMonUpper32TotalOctets_Type()
)
rptrMonUpper32TotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonUpper32TotalOctets.setStatus("current")
_RptrMonHCTotalOctets_Type = Counter64
_RptrMonHCTotalOctets_Object = MibTableColumn
rptrMonHCTotalOctets = _RptrMonHCTotalOctets_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 4, 2, 1, 2),
    _RptrMonHCTotalOctets_Type()
)
rptrMonHCTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonHCTotalOctets.setStatus("current")
_RptrAddrTrackPackage_ObjectIdentity = ObjectIdentity
rptrAddrTrackPackage = _RptrAddrTrackPackage_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 3)
)
_RptrAddrTrackRptrInfo_ObjectIdentity = ObjectIdentity
rptrAddrTrackRptrInfo = _RptrAddrTrackRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 3, 1)
)
_RptrAddrSearchTable_Object = MibTable
rptrAddrSearchTable = _RptrAddrSearchTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 1, 1)
)
if mibBuilder.loadTexts:
    rptrAddrSearchTable.setStatus("current")
_RptrAddrSearchEntry_Object = MibTableRow
rptrAddrSearchEntry = _RptrAddrSearchEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 1, 1, 1)
)
rptrAddrSearchEntry.setIndexNames(
    (0, "SNMP-REPEATER-MIB", "rptrInfoId"),
)
if mibBuilder.loadTexts:
    rptrAddrSearchEntry.setStatus("current")
_RptrAddrSearchLock_Type = TestAndIncr
_RptrAddrSearchLock_Object = MibTableColumn
rptrAddrSearchLock = _RptrAddrSearchLock_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 1, 1, 1, 1),
    _RptrAddrSearchLock_Type()
)
rptrAddrSearchLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrAddrSearchLock.setStatus("current")


class _RptrAddrSearchStatus_Type(Integer32):
    """Custom type rptrAddrSearchStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInUse", 1),
          ("inUse", 2))
    )


_RptrAddrSearchStatus_Type.__name__ = "Integer32"
_RptrAddrSearchStatus_Object = MibTableColumn
rptrAddrSearchStatus = _RptrAddrSearchStatus_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 1, 1, 1, 2),
    _RptrAddrSearchStatus_Type()
)
rptrAddrSearchStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrAddrSearchStatus.setStatus("current")
_RptrAddrSearchAddress_Type = MacAddress
_RptrAddrSearchAddress_Object = MibTableColumn
rptrAddrSearchAddress = _RptrAddrSearchAddress_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 1, 1, 1, 3),
    _RptrAddrSearchAddress_Type()
)
rptrAddrSearchAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrAddrSearchAddress.setStatus("current")


class _RptrAddrSearchState_Type(Integer32):
    """Custom type rptrAddrSearchState based on Integer32"""
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
          ("single", 2),
          ("multiple", 3))
    )


_RptrAddrSearchState_Type.__name__ = "Integer32"
_RptrAddrSearchState_Object = MibTableColumn
rptrAddrSearchState = _RptrAddrSearchState_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 1, 1, 1, 4),
    _RptrAddrSearchState_Type()
)
rptrAddrSearchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrAddrSearchState.setStatus("current")


class _RptrAddrSearchGroup_Type(Integer32):
    """Custom type rptrAddrSearchGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RptrAddrSearchGroup_Type.__name__ = "Integer32"
_RptrAddrSearchGroup_Object = MibTableColumn
rptrAddrSearchGroup = _RptrAddrSearchGroup_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 1, 1, 1, 5),
    _RptrAddrSearchGroup_Type()
)
rptrAddrSearchGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrAddrSearchGroup.setStatus("current")


class _RptrAddrSearchPort_Type(Integer32):
    """Custom type rptrAddrSearchPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RptrAddrSearchPort_Type.__name__ = "Integer32"
_RptrAddrSearchPort_Object = MibTableColumn
rptrAddrSearchPort = _RptrAddrSearchPort_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 1, 1, 1, 6),
    _RptrAddrSearchPort_Type()
)
rptrAddrSearchPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrAddrSearchPort.setStatus("current")
_RptrAddrSearchOwner_Type = OwnerString
_RptrAddrSearchOwner_Object = MibTableColumn
rptrAddrSearchOwner = _RptrAddrSearchOwner_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 1, 1, 1, 7),
    _RptrAddrSearchOwner_Type()
)
rptrAddrSearchOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrAddrSearchOwner.setStatus("current")
_RptrAddrTrackGroupInfo_ObjectIdentity = ObjectIdentity
rptrAddrTrackGroupInfo = _RptrAddrTrackGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 3, 2)
)
_RptrAddrTrackPortInfo_ObjectIdentity = ObjectIdentity
rptrAddrTrackPortInfo = _RptrAddrTrackPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 3, 3)
)
_RptrAddrTrackTable_Object = MibTable
rptrAddrTrackTable = _RptrAddrTrackTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1)
)
if mibBuilder.loadTexts:
    rptrAddrTrackTable.setStatus("current")
_RptrAddrTrackEntry_Object = MibTableRow
rptrAddrTrackEntry = _RptrAddrTrackEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1)
)
rptrAddrTrackEntry.setIndexNames(
    (0, "SNMP-REPEATER-MIB", "rptrAddrTrackGroupIndex"),
    (0, "SNMP-REPEATER-MIB", "rptrAddrTrackPortIndex"),
)
if mibBuilder.loadTexts:
    rptrAddrTrackEntry.setStatus("current")


class _RptrAddrTrackGroupIndex_Type(Integer32):
    """Custom type rptrAddrTrackGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RptrAddrTrackGroupIndex_Type.__name__ = "Integer32"
_RptrAddrTrackGroupIndex_Object = MibTableColumn
rptrAddrTrackGroupIndex = _RptrAddrTrackGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 1),
    _RptrAddrTrackGroupIndex_Type()
)
rptrAddrTrackGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrAddrTrackGroupIndex.setStatus("current")


class _RptrAddrTrackPortIndex_Type(Integer32):
    """Custom type rptrAddrTrackPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RptrAddrTrackPortIndex_Type.__name__ = "Integer32"
_RptrAddrTrackPortIndex_Object = MibTableColumn
rptrAddrTrackPortIndex = _RptrAddrTrackPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 2),
    _RptrAddrTrackPortIndex_Type()
)
rptrAddrTrackPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrAddrTrackPortIndex.setStatus("current")
_RptrAddrTrackLastSourceAddress_Type = MacAddress
_RptrAddrTrackLastSourceAddress_Object = MibTableColumn
rptrAddrTrackLastSourceAddress = _RptrAddrTrackLastSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 3),
    _RptrAddrTrackLastSourceAddress_Type()
)
rptrAddrTrackLastSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrAddrTrackLastSourceAddress.setStatus("deprecated")
_RptrAddrTrackSourceAddrChanges_Type = Counter32
_RptrAddrTrackSourceAddrChanges_Object = MibTableColumn
rptrAddrTrackSourceAddrChanges = _RptrAddrTrackSourceAddrChanges_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 4),
    _RptrAddrTrackSourceAddrChanges_Type()
)
rptrAddrTrackSourceAddrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrAddrTrackSourceAddrChanges.setStatus("current")
_RptrAddrTrackNewLastSrcAddress_Type = OptMacAddr
_RptrAddrTrackNewLastSrcAddress_Object = MibTableColumn
rptrAddrTrackNewLastSrcAddress = _RptrAddrTrackNewLastSrcAddress_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 5),
    _RptrAddrTrackNewLastSrcAddress_Type()
)
rptrAddrTrackNewLastSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrAddrTrackNewLastSrcAddress.setStatus("current")
_RptrAddrTrackCapacity_Type = Integer32
_RptrAddrTrackCapacity_Object = MibTableColumn
rptrAddrTrackCapacity = _RptrAddrTrackCapacity_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 6),
    _RptrAddrTrackCapacity_Type()
)
rptrAddrTrackCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrAddrTrackCapacity.setStatus("current")
_RptrExtAddrTrackTable_Object = MibTable
rptrExtAddrTrackTable = _RptrExtAddrTrackTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 2)
)
if mibBuilder.loadTexts:
    rptrExtAddrTrackTable.setStatus("current")
_RptrExtAddrTrackEntry_Object = MibTableRow
rptrExtAddrTrackEntry = _RptrExtAddrTrackEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 2, 1)
)
rptrExtAddrTrackEntry.setIndexNames(
    (0, "SNMP-REPEATER-MIB", "rptrAddrTrackGroupIndex"),
    (0, "SNMP-REPEATER-MIB", "rptrAddrTrackPortIndex"),
    (0, "SNMP-REPEATER-MIB", "rptrExtAddrTrackMacIndex"),
)
if mibBuilder.loadTexts:
    rptrExtAddrTrackEntry.setStatus("current")


class _RptrExtAddrTrackMacIndex_Type(Integer32):
    """Custom type rptrExtAddrTrackMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RptrExtAddrTrackMacIndex_Type.__name__ = "Integer32"
_RptrExtAddrTrackMacIndex_Object = MibTableColumn
rptrExtAddrTrackMacIndex = _RptrExtAddrTrackMacIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 2, 1, 1),
    _RptrExtAddrTrackMacIndex_Type()
)
rptrExtAddrTrackMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrExtAddrTrackMacIndex.setStatus("current")
_RptrExtAddrTrackSourceAddress_Type = MacAddress
_RptrExtAddrTrackSourceAddress_Object = MibTableColumn
rptrExtAddrTrackSourceAddress = _RptrExtAddrTrackSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 2, 1, 2),
    _RptrExtAddrTrackSourceAddress_Type()
)
rptrExtAddrTrackSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrExtAddrTrackSourceAddress.setStatus("current")
_RptrTopNPackage_ObjectIdentity = ObjectIdentity
rptrTopNPackage = _RptrTopNPackage_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 4)
)
_RptrTopNRptrInfo_ObjectIdentity = ObjectIdentity
rptrTopNRptrInfo = _RptrTopNRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 4, 1)
)
_RptrTopNGroupInfo_ObjectIdentity = ObjectIdentity
rptrTopNGroupInfo = _RptrTopNGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 4, 2)
)
_RptrTopNPortInfo_ObjectIdentity = ObjectIdentity
rptrTopNPortInfo = _RptrTopNPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 4, 3)
)
_RptrTopNPortControlTable_Object = MibTable
rptrTopNPortControlTable = _RptrTopNPortControlTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 4, 3, 1)
)
if mibBuilder.loadTexts:
    rptrTopNPortControlTable.setStatus("current")
_RptrTopNPortControlEntry_Object = MibTableRow
rptrTopNPortControlEntry = _RptrTopNPortControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 4, 3, 1, 1)
)
rptrTopNPortControlEntry.setIndexNames(
    (0, "SNMP-REPEATER-MIB", "rptrTopNPortControlIndex"),
)
if mibBuilder.loadTexts:
    rptrTopNPortControlEntry.setStatus("current")


class _RptrTopNPortControlIndex_Type(Integer32):
    """Custom type rptrTopNPortControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RptrTopNPortControlIndex_Type.__name__ = "Integer32"
_RptrTopNPortControlIndex_Object = MibTableColumn
rptrTopNPortControlIndex = _RptrTopNPortControlIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 4, 3, 1, 1, 1),
    _RptrTopNPortControlIndex_Type()
)
rptrTopNPortControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrTopNPortControlIndex.setStatus("current")


class _RptrTopNPortRepeaterId_Type(Integer32):
    """Custom type rptrTopNPortRepeaterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RptrTopNPortRepeaterId_Type.__name__ = "Integer32"
_RptrTopNPortRepeaterId_Object = MibTableColumn
rptrTopNPortRepeaterId = _RptrTopNPortRepeaterId_Object(
    (1, 3, 6, 1, 2, 1, 22, 4, 3, 1, 1, 2),
    _RptrTopNPortRepeaterId_Type()
)
rptrTopNPortRepeaterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rptrTopNPortRepeaterId.setStatus("current")


class _RptrTopNPortRateBase_Type(Integer32):
    """Custom type rptrTopNPortRateBase based on Integer32"""
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
        *(("readableFrames", 1),
          ("readableOctets", 2),
          ("fcsErrors", 3),
          ("alignmentErrors", 4),
          ("frameTooLongs", 5),
          ("shortEvents", 6),
          ("runts", 7),
          ("collisions", 8),
          ("lateEvents", 9),
          ("veryLongEvents", 10),
          ("dataRateMismatches", 11),
          ("autoPartitions", 12),
          ("totalErrors", 13),
          ("isolates", 14),
          ("symbolErrors", 15))
    )


_RptrTopNPortRateBase_Type.__name__ = "Integer32"
_RptrTopNPortRateBase_Object = MibTableColumn
rptrTopNPortRateBase = _RptrTopNPortRateBase_Object(
    (1, 3, 6, 1, 2, 1, 22, 4, 3, 1, 1, 3),
    _RptrTopNPortRateBase_Type()
)
rptrTopNPortRateBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rptrTopNPortRateBase.setStatus("current")


class _RptrTopNPortTimeRemaining_Type(Integer32):
    """Custom type rptrTopNPortTimeRemaining based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RptrTopNPortTimeRemaining_Type.__name__ = "Integer32"
_RptrTopNPortTimeRemaining_Object = MibTableColumn
rptrTopNPortTimeRemaining = _RptrTopNPortTimeRemaining_Object(
    (1, 3, 6, 1, 2, 1, 22, 4, 3, 1, 1, 4),
    _RptrTopNPortTimeRemaining_Type()
)
rptrTopNPortTimeRemaining.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rptrTopNPortTimeRemaining.setStatus("current")


class _RptrTopNPortDuration_Type(Integer32):
    """Custom type rptrTopNPortDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RptrTopNPortDuration_Type.__name__ = "Integer32"
_RptrTopNPortDuration_Object = MibTableColumn
rptrTopNPortDuration = _RptrTopNPortDuration_Object(
    (1, 3, 6, 1, 2, 1, 22, 4, 3, 1, 1, 5),
    _RptrTopNPortDuration_Type()
)
rptrTopNPortDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrTopNPortDuration.setStatus("current")


class _RptrTopNPortRequestedSize_Type(Integer32):
    """Custom type rptrTopNPortRequestedSize based on Integer32"""
    defaultValue = 10


_RptrTopNPortRequestedSize_Type.__name__ = "Integer32"
_RptrTopNPortRequestedSize_Object = MibTableColumn
rptrTopNPortRequestedSize = _RptrTopNPortRequestedSize_Object(
    (1, 3, 6, 1, 2, 1, 22, 4, 3, 1, 1, 6),
    _RptrTopNPortRequestedSize_Type()
)
rptrTopNPortRequestedSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rptrTopNPortRequestedSize.setStatus("current")


class _RptrTopNPortGrantedSize_Type(Integer32):
    """Custom type rptrTopNPortGrantedSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RptrTopNPortGrantedSize_Type.__name__ = "Integer32"
_RptrTopNPortGrantedSize_Object = MibTableColumn
rptrTopNPortGrantedSize = _RptrTopNPortGrantedSize_Object(
    (1, 3, 6, 1, 2, 1, 22, 4, 3, 1, 1, 7),
    _RptrTopNPortGrantedSize_Type()
)
rptrTopNPortGrantedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrTopNPortGrantedSize.setStatus("current")
_RptrTopNPortStartTime_Type = TimeStamp
_RptrTopNPortStartTime_Object = MibTableColumn
rptrTopNPortStartTime = _RptrTopNPortStartTime_Object(
    (1, 3, 6, 1, 2, 1, 22, 4, 3, 1, 1, 8),
    _RptrTopNPortStartTime_Type()
)
rptrTopNPortStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrTopNPortStartTime.setStatus("current")
_RptrTopNPortOwner_Type = OwnerString
_RptrTopNPortOwner_Object = MibTableColumn
rptrTopNPortOwner = _RptrTopNPortOwner_Object(
    (1, 3, 6, 1, 2, 1, 22, 4, 3, 1, 1, 9),
    _RptrTopNPortOwner_Type()
)
rptrTopNPortOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rptrTopNPortOwner.setStatus("current")
_RptrTopNPortRowStatus_Type = RowStatus
_RptrTopNPortRowStatus_Object = MibTableColumn
rptrTopNPortRowStatus = _RptrTopNPortRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 22, 4, 3, 1, 1, 10),
    _RptrTopNPortRowStatus_Type()
)
rptrTopNPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rptrTopNPortRowStatus.setStatus("current")
_RptrTopNPortTable_Object = MibTable
rptrTopNPortTable = _RptrTopNPortTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 4, 3, 2)
)
if mibBuilder.loadTexts:
    rptrTopNPortTable.setStatus("current")
_RptrTopNPortEntry_Object = MibTableRow
rptrTopNPortEntry = _RptrTopNPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 4, 3, 2, 1)
)
rptrTopNPortEntry.setIndexNames(
    (0, "SNMP-REPEATER-MIB", "rptrTopNPortControlIndex"),
    (0, "SNMP-REPEATER-MIB", "rptrTopNPortIndex"),
)
if mibBuilder.loadTexts:
    rptrTopNPortEntry.setStatus("current")


class _RptrTopNPortIndex_Type(Integer32):
    """Custom type rptrTopNPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RptrTopNPortIndex_Type.__name__ = "Integer32"
_RptrTopNPortIndex_Object = MibTableColumn
rptrTopNPortIndex = _RptrTopNPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 4, 3, 2, 1, 1),
    _RptrTopNPortIndex_Type()
)
rptrTopNPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrTopNPortIndex.setStatus("current")


class _RptrTopNPortGroupIndex_Type(Integer32):
    """Custom type rptrTopNPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RptrTopNPortGroupIndex_Type.__name__ = "Integer32"
_RptrTopNPortGroupIndex_Object = MibTableColumn
rptrTopNPortGroupIndex = _RptrTopNPortGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 4, 3, 2, 1, 2),
    _RptrTopNPortGroupIndex_Type()
)
rptrTopNPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrTopNPortGroupIndex.setStatus("current")


class _RptrTopNPortPortIndex_Type(Integer32):
    """Custom type rptrTopNPortPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RptrTopNPortPortIndex_Type.__name__ = "Integer32"
_RptrTopNPortPortIndex_Object = MibTableColumn
rptrTopNPortPortIndex = _RptrTopNPortPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 4, 3, 2, 1, 3),
    _RptrTopNPortPortIndex_Type()
)
rptrTopNPortPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrTopNPortPortIndex.setStatus("current")
_RptrTopNPortRate_Type = Gauge32
_RptrTopNPortRate_Object = MibTableColumn
rptrTopNPortRate = _RptrTopNPortRate_Object(
    (1, 3, 6, 1, 2, 1, 22, 4, 3, 2, 1, 4),
    _RptrTopNPortRate_Type()
)
rptrTopNPortRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrTopNPortRate.setStatus("current")
_SnmpRptrModConf_ObjectIdentity = ObjectIdentity
snmpRptrModConf = _SnmpRptrModConf_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 5, 1)
)
_SnmpRptrModCompls_ObjectIdentity = ObjectIdentity
snmpRptrModCompls = _SnmpRptrModCompls_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 5, 1, 1)
)
_SnmpRptrModObjGrps_ObjectIdentity = ObjectIdentity
snmpRptrModObjGrps = _SnmpRptrModObjGrps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 5, 1, 2)
)
_SnmpRptrModNotGrps_ObjectIdentity = ObjectIdentity
snmpRptrModNotGrps = _SnmpRptrModNotGrps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 5, 1, 3)
)

# Managed Objects groups

snmpRptrGrpBasic1516 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 22, 5, 1, 2, 1)
)
snmpRptrGrpBasic1516.setObjects(
      *(("SNMP-REPEATER-MIB", "rptrGroupCapacity"),
        ("SNMP-REPEATER-MIB", "rptrOperStatus"),
        ("SNMP-REPEATER-MIB", "rptrHealthText"),
        ("SNMP-REPEATER-MIB", "rptrReset"),
        ("SNMP-REPEATER-MIB", "rptrNonDisruptTest"),
        ("SNMP-REPEATER-MIB", "rptrTotalPartitionedPorts"),
        ("SNMP-REPEATER-MIB", "rptrGroupIndex"),
        ("SNMP-REPEATER-MIB", "rptrGroupDescr"),
        ("SNMP-REPEATER-MIB", "rptrGroupObjectID"),
        ("SNMP-REPEATER-MIB", "rptrGroupOperStatus"),
        ("SNMP-REPEATER-MIB", "rptrGroupLastOperStatusChange"),
        ("SNMP-REPEATER-MIB", "rptrGroupPortCapacity"),
        ("SNMP-REPEATER-MIB", "rptrPortGroupIndex"),
        ("SNMP-REPEATER-MIB", "rptrPortIndex"),
        ("SNMP-REPEATER-MIB", "rptrPortAdminStatus"),
        ("SNMP-REPEATER-MIB", "rptrPortAutoPartitionState"),
        ("SNMP-REPEATER-MIB", "rptrPortOperStatus"))
)
if mibBuilder.loadTexts:
    snmpRptrGrpBasic1516.setStatus("deprecated")

snmpRptrGrpMonitor1516 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 22, 5, 1, 2, 2)
)
snmpRptrGrpMonitor1516.setObjects(
      *(("SNMP-REPEATER-MIB", "rptrMonitorTransmitCollisions"),
        ("SNMP-REPEATER-MIB", "rptrMonitorGroupIndex"),
        ("SNMP-REPEATER-MIB", "rptrMonitorGroupTotalFrames"),
        ("SNMP-REPEATER-MIB", "rptrMonitorGroupTotalOctets"),
        ("SNMP-REPEATER-MIB", "rptrMonitorGroupTotalErrors"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortGroupIndex"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortIndex"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortReadableFrames"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortReadableOctets"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortFCSErrors"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortAlignmentErrors"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortFrameTooLongs"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortShortEvents"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortRunts"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortCollisions"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortLateEvents"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortVeryLongEvents"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortDataRateMismatches"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortAutoPartitions"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortTotalErrors"))
)
if mibBuilder.loadTexts:
    snmpRptrGrpMonitor1516.setStatus("deprecated")

snmpRptrGrpAddrTrack1368 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 22, 5, 1, 2, 3)
)
snmpRptrGrpAddrTrack1368.setObjects(
      *(("SNMP-REPEATER-MIB", "rptrAddrTrackGroupIndex"),
        ("SNMP-REPEATER-MIB", "rptrAddrTrackPortIndex"),
        ("SNMP-REPEATER-MIB", "rptrAddrTrackLastSourceAddress"),
        ("SNMP-REPEATER-MIB", "rptrAddrTrackSourceAddrChanges"))
)
if mibBuilder.loadTexts:
    snmpRptrGrpAddrTrack1368.setStatus("obsolete")

snmpRptrGrpAddrTrack1516 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 22, 5, 1, 2, 4)
)
snmpRptrGrpAddrTrack1516.setObjects(
      *(("SNMP-REPEATER-MIB", "rptrAddrTrackGroupIndex"),
        ("SNMP-REPEATER-MIB", "rptrAddrTrackPortIndex"),
        ("SNMP-REPEATER-MIB", "rptrAddrTrackLastSourceAddress"),
        ("SNMP-REPEATER-MIB", "rptrAddrTrackSourceAddrChanges"),
        ("SNMP-REPEATER-MIB", "rptrAddrTrackNewLastSrcAddress"))
)
if mibBuilder.loadTexts:
    snmpRptrGrpAddrTrack1516.setStatus("deprecated")

snmpRptrGrpBasic = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 22, 5, 1, 2, 5)
)
snmpRptrGrpBasic.setObjects(
      *(("SNMP-REPEATER-MIB", "rptrGroupIndex"),
        ("SNMP-REPEATER-MIB", "rptrGroupObjectID"),
        ("SNMP-REPEATER-MIB", "rptrGroupOperStatus"),
        ("SNMP-REPEATER-MIB", "rptrGroupPortCapacity"),
        ("SNMP-REPEATER-MIB", "rptrPortGroupIndex"),
        ("SNMP-REPEATER-MIB", "rptrPortIndex"),
        ("SNMP-REPEATER-MIB", "rptrPortAdminStatus"),
        ("SNMP-REPEATER-MIB", "rptrPortAutoPartitionState"),
        ("SNMP-REPEATER-MIB", "rptrPortOperStatus"),
        ("SNMP-REPEATER-MIB", "rptrPortRptrId"),
        ("SNMP-REPEATER-MIB", "rptrInfoId"),
        ("SNMP-REPEATER-MIB", "rptrInfoRptrType"),
        ("SNMP-REPEATER-MIB", "rptrInfoOperStatus"),
        ("SNMP-REPEATER-MIB", "rptrInfoReset"),
        ("SNMP-REPEATER-MIB", "rptrInfoPartitionedPorts"),
        ("SNMP-REPEATER-MIB", "rptrInfoLastChange"))
)
if mibBuilder.loadTexts:
    snmpRptrGrpBasic.setStatus("current")

snmpRptrGrpMonitor = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 22, 5, 1, 2, 6)
)
snmpRptrGrpMonitor.setObjects(
      *(("SNMP-REPEATER-MIB", "rptrMonitorPortGroupIndex"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortIndex"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortReadableFrames"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortReadableOctets"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortFCSErrors"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortAlignmentErrors"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortFrameTooLongs"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortShortEvents"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortRunts"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortCollisions"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortLateEvents"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortVeryLongEvents"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortDataRateMismatches"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortAutoPartitions"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortTotalErrors"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortLastChange"),
        ("SNMP-REPEATER-MIB", "rptrMonTxCollisions"),
        ("SNMP-REPEATER-MIB", "rptrMonTotalFrames"),
        ("SNMP-REPEATER-MIB", "rptrMonTotalErrors"),
        ("SNMP-REPEATER-MIB", "rptrMonTotalOctets"))
)
if mibBuilder.loadTexts:
    snmpRptrGrpMonitor.setStatus("current")

snmpRptrGrpMonitor100 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 22, 5, 1, 2, 7)
)
snmpRptrGrpMonitor100.setObjects(
      *(("SNMP-REPEATER-MIB", "rptrMonitorPortIsolates"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortSymbolErrors"),
        ("SNMP-REPEATER-MIB", "rptrMonitorPortUpper32Octets"),
        ("SNMP-REPEATER-MIB", "rptrMonUpper32TotalOctets"))
)
if mibBuilder.loadTexts:
    snmpRptrGrpMonitor100.setStatus("current")

snmpRptrGrpMonitor100w64 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 22, 5, 1, 2, 8)
)
snmpRptrGrpMonitor100w64.setObjects(
      *(("SNMP-REPEATER-MIB", "rptrMonitorPortHCReadableOctets"),
        ("SNMP-REPEATER-MIB", "rptrMonHCTotalOctets"))
)
if mibBuilder.loadTexts:
    snmpRptrGrpMonitor100w64.setStatus("current")

snmpRptrGrpAddrTrack = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 22, 5, 1, 2, 9)
)
snmpRptrGrpAddrTrack.setObjects(
      *(("SNMP-REPEATER-MIB", "rptrAddrTrackGroupIndex"),
        ("SNMP-REPEATER-MIB", "rptrAddrTrackPortIndex"),
        ("SNMP-REPEATER-MIB", "rptrAddrTrackSourceAddrChanges"),
        ("SNMP-REPEATER-MIB", "rptrAddrTrackNewLastSrcAddress"),
        ("SNMP-REPEATER-MIB", "rptrAddrTrackCapacity"))
)
if mibBuilder.loadTexts:
    snmpRptrGrpAddrTrack.setStatus("current")

snmpRptrGrpExtAddrTrack = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 22, 5, 1, 2, 10)
)
snmpRptrGrpExtAddrTrack.setObjects(
      *(("SNMP-REPEATER-MIB", "rptrExtAddrTrackMacIndex"),
        ("SNMP-REPEATER-MIB", "rptrExtAddrTrackSourceAddress"))
)
if mibBuilder.loadTexts:
    snmpRptrGrpExtAddrTrack.setStatus("current")

snmpRptrGrpRptrAddrSearch = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 22, 5, 1, 2, 11)
)
snmpRptrGrpRptrAddrSearch.setObjects(
      *(("SNMP-REPEATER-MIB", "rptrAddrSearchLock"),
        ("SNMP-REPEATER-MIB", "rptrAddrSearchStatus"),
        ("SNMP-REPEATER-MIB", "rptrAddrSearchAddress"),
        ("SNMP-REPEATER-MIB", "rptrAddrSearchState"),
        ("SNMP-REPEATER-MIB", "rptrAddrSearchGroup"),
        ("SNMP-REPEATER-MIB", "rptrAddrSearchPort"),
        ("SNMP-REPEATER-MIB", "rptrAddrSearchOwner"))
)
if mibBuilder.loadTexts:
    snmpRptrGrpRptrAddrSearch.setStatus("current")

snmpRptrGrpTopNPort = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 22, 5, 1, 2, 12)
)
snmpRptrGrpTopNPort.setObjects(
      *(("SNMP-REPEATER-MIB", "rptrTopNPortControlIndex"),
        ("SNMP-REPEATER-MIB", "rptrTopNPortRepeaterId"),
        ("SNMP-REPEATER-MIB", "rptrTopNPortRateBase"),
        ("SNMP-REPEATER-MIB", "rptrTopNPortTimeRemaining"),
        ("SNMP-REPEATER-MIB", "rptrTopNPortDuration"),
        ("SNMP-REPEATER-MIB", "rptrTopNPortRequestedSize"),
        ("SNMP-REPEATER-MIB", "rptrTopNPortGrantedSize"),
        ("SNMP-REPEATER-MIB", "rptrTopNPortStartTime"),
        ("SNMP-REPEATER-MIB", "rptrTopNPortOwner"),
        ("SNMP-REPEATER-MIB", "rptrTopNPortRowStatus"),
        ("SNMP-REPEATER-MIB", "rptrTopNPortIndex"),
        ("SNMP-REPEATER-MIB", "rptrTopNPortGroupIndex"),
        ("SNMP-REPEATER-MIB", "rptrTopNPortPortIndex"),
        ("SNMP-REPEATER-MIB", "rptrTopNPortRate"))
)
if mibBuilder.loadTexts:
    snmpRptrGrpTopNPort.setStatus("current")


# Notification objects

rptrHealth = NotificationType(
    (1, 3, 6, 1, 2, 1, 22, 0, 1)
)
rptrHealth.setObjects(
    ("SNMP-REPEATER-MIB", "rptrOperStatus")
)
if mibBuilder.loadTexts:
    rptrHealth.setStatus(
        "deprecated"
    )

rptrGroupChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 22, 0, 2)
)
rptrGroupChange.setObjects(
    ("SNMP-REPEATER-MIB", "rptrGroupIndex")
)
if mibBuilder.loadTexts:
    rptrGroupChange.setStatus(
        "deprecated"
    )

rptrResetEvent = NotificationType(
    (1, 3, 6, 1, 2, 1, 22, 0, 3)
)
rptrResetEvent.setObjects(
    ("SNMP-REPEATER-MIB", "rptrOperStatus")
)
if mibBuilder.loadTexts:
    rptrResetEvent.setStatus(
        "deprecated"
    )

rptrInfoHealth = NotificationType(
    (1, 3, 6, 1, 2, 1, 22, 0, 4)
)
rptrInfoHealth.setObjects(
    ("SNMP-REPEATER-MIB", "rptrInfoOperStatus")
)
if mibBuilder.loadTexts:
    rptrInfoHealth.setStatus(
        "current"
    )

rptrInfoResetEvent = NotificationType(
    (1, 3, 6, 1, 2, 1, 22, 0, 5)
)
rptrInfoResetEvent.setObjects(
    ("SNMP-REPEATER-MIB", "rptrInfoOperStatus")
)
if mibBuilder.loadTexts:
    rptrInfoResetEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

snmpRptrModComplRFC1368 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 22, 5, 1, 1, 1)
)
snmpRptrModComplRFC1368.setObjects(
      *(("SNMP-REPEATER-MIB", "snmpRptrGrpBasic1516"),
        ("SNMP-REPEATER-MIB", "snmpRptrGrpMonitor1516"),
        ("SNMP-REPEATER-MIB", "snmpRptrGrpAddrTrack1368"))
)
if mibBuilder.loadTexts:
    snmpRptrModComplRFC1368.setStatus(
        "obsolete"
    )

snmpRptrModComplRFC1516 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 22, 5, 1, 1, 2)
)
snmpRptrModComplRFC1516.setObjects(
      *(("SNMP-REPEATER-MIB", "snmpRptrGrpBasic1516"),
        ("SNMP-REPEATER-MIB", "snmpRptrGrpMonitor1516"),
        ("SNMP-REPEATER-MIB", "snmpRptrGrpAddrTrack1516"))
)
if mibBuilder.loadTexts:
    snmpRptrModComplRFC1516.setStatus(
        "deprecated"
    )

snmpRptrModCompl = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 22, 5, 1, 1, 3)
)
snmpRptrModCompl.setObjects(
      *(("SNMP-REPEATER-MIB", "snmpRptrGrpBasic"),
        ("SNMP-REPEATER-MIB", "snmpRptrGrpMonitor"),
        ("SNMP-REPEATER-MIB", "snmpRptrGrpAddrTrack"),
        ("SNMP-REPEATER-MIB", "snmpRptrGrpMonitor100"),
        ("SNMP-REPEATER-MIB", "snmpRptrGrpMonitor100w64"),
        ("SNMP-REPEATER-MIB", "snmpRptrGrpExtAddrTrack"),
        ("SNMP-REPEATER-MIB", "snmpRptrGrpRptrAddrSearch"),
        ("SNMP-REPEATER-MIB", "snmpRptrGrpTopNPort"))
)
if mibBuilder.loadTexts:
    snmpRptrModCompl.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP-REPEATER-MIB",
    **{"OptMacAddr": OptMacAddr,
       "snmpDot3RptrMgt": snmpDot3RptrMgt,
       "rptrHealth": rptrHealth,
       "rptrGroupChange": rptrGroupChange,
       "rptrResetEvent": rptrResetEvent,
       "rptrInfoHealth": rptrInfoHealth,
       "rptrInfoResetEvent": rptrInfoResetEvent,
       "rptrBasicPackage": rptrBasicPackage,
       "rptrRptrInfo": rptrRptrInfo,
       "rptrGroupCapacity": rptrGroupCapacity,
       "rptrOperStatus": rptrOperStatus,
       "rptrHealthText": rptrHealthText,
       "rptrReset": rptrReset,
       "rptrNonDisruptTest": rptrNonDisruptTest,
       "rptrTotalPartitionedPorts": rptrTotalPartitionedPorts,
       "rptrGroupInfo": rptrGroupInfo,
       "rptrGroupTable": rptrGroupTable,
       "rptrGroupEntry": rptrGroupEntry,
       "rptrGroupIndex": rptrGroupIndex,
       "rptrGroupDescr": rptrGroupDescr,
       "rptrGroupObjectID": rptrGroupObjectID,
       "rptrGroupOperStatus": rptrGroupOperStatus,
       "rptrGroupLastOperStatusChange": rptrGroupLastOperStatusChange,
       "rptrGroupPortCapacity": rptrGroupPortCapacity,
       "rptrPortInfo": rptrPortInfo,
       "rptrPortTable": rptrPortTable,
       "rptrPortEntry": rptrPortEntry,
       "rptrPortGroupIndex": rptrPortGroupIndex,
       "rptrPortIndex": rptrPortIndex,
       "rptrPortAdminStatus": rptrPortAdminStatus,
       "rptrPortAutoPartitionState": rptrPortAutoPartitionState,
       "rptrPortOperStatus": rptrPortOperStatus,
       "rptrPortRptrId": rptrPortRptrId,
       "rptrAllRptrInfo": rptrAllRptrInfo,
       "rptrInfoTable": rptrInfoTable,
       "rptrInfoEntry": rptrInfoEntry,
       "rptrInfoId": rptrInfoId,
       "rptrInfoRptrType": rptrInfoRptrType,
       "rptrInfoOperStatus": rptrInfoOperStatus,
       "rptrInfoReset": rptrInfoReset,
       "rptrInfoPartitionedPorts": rptrInfoPartitionedPorts,
       "rptrInfoLastChange": rptrInfoLastChange,
       "rptrMonitorPackage": rptrMonitorPackage,
       "rptrMonitorRptrInfo": rptrMonitorRptrInfo,
       "rptrMonitorTransmitCollisions": rptrMonitorTransmitCollisions,
       "rptrMonitorGroupInfo": rptrMonitorGroupInfo,
       "rptrMonitorGroupTable": rptrMonitorGroupTable,
       "rptrMonitorGroupEntry": rptrMonitorGroupEntry,
       "rptrMonitorGroupIndex": rptrMonitorGroupIndex,
       "rptrMonitorGroupTotalFrames": rptrMonitorGroupTotalFrames,
       "rptrMonitorGroupTotalOctets": rptrMonitorGroupTotalOctets,
       "rptrMonitorGroupTotalErrors": rptrMonitorGroupTotalErrors,
       "rptrMonitorPortInfo": rptrMonitorPortInfo,
       "rptrMonitorPortTable": rptrMonitorPortTable,
       "rptrMonitorPortEntry": rptrMonitorPortEntry,
       "rptrMonitorPortGroupIndex": rptrMonitorPortGroupIndex,
       "rptrMonitorPortIndex": rptrMonitorPortIndex,
       "rptrMonitorPortReadableFrames": rptrMonitorPortReadableFrames,
       "rptrMonitorPortReadableOctets": rptrMonitorPortReadableOctets,
       "rptrMonitorPortFCSErrors": rptrMonitorPortFCSErrors,
       "rptrMonitorPortAlignmentErrors": rptrMonitorPortAlignmentErrors,
       "rptrMonitorPortFrameTooLongs": rptrMonitorPortFrameTooLongs,
       "rptrMonitorPortShortEvents": rptrMonitorPortShortEvents,
       "rptrMonitorPortRunts": rptrMonitorPortRunts,
       "rptrMonitorPortCollisions": rptrMonitorPortCollisions,
       "rptrMonitorPortLateEvents": rptrMonitorPortLateEvents,
       "rptrMonitorPortVeryLongEvents": rptrMonitorPortVeryLongEvents,
       "rptrMonitorPortDataRateMismatches": rptrMonitorPortDataRateMismatches,
       "rptrMonitorPortAutoPartitions": rptrMonitorPortAutoPartitions,
       "rptrMonitorPortTotalErrors": rptrMonitorPortTotalErrors,
       "rptrMonitorPortLastChange": rptrMonitorPortLastChange,
       "rptrMonitor100PortTable": rptrMonitor100PortTable,
       "rptrMonitor100PortEntry": rptrMonitor100PortEntry,
       "rptrMonitorPortIsolates": rptrMonitorPortIsolates,
       "rptrMonitorPortSymbolErrors": rptrMonitorPortSymbolErrors,
       "rptrMonitorPortUpper32Octets": rptrMonitorPortUpper32Octets,
       "rptrMonitorPortHCReadableOctets": rptrMonitorPortHCReadableOctets,
       "rptrMonitorAllRptrInfo": rptrMonitorAllRptrInfo,
       "rptrMonTable": rptrMonTable,
       "rptrMonEntry": rptrMonEntry,
       "rptrMonTxCollisions": rptrMonTxCollisions,
       "rptrMonTotalFrames": rptrMonTotalFrames,
       "rptrMonTotalErrors": rptrMonTotalErrors,
       "rptrMonTotalOctets": rptrMonTotalOctets,
       "rptrMon100Table": rptrMon100Table,
       "rptrMon100Entry": rptrMon100Entry,
       "rptrMonUpper32TotalOctets": rptrMonUpper32TotalOctets,
       "rptrMonHCTotalOctets": rptrMonHCTotalOctets,
       "rptrAddrTrackPackage": rptrAddrTrackPackage,
       "rptrAddrTrackRptrInfo": rptrAddrTrackRptrInfo,
       "rptrAddrSearchTable": rptrAddrSearchTable,
       "rptrAddrSearchEntry": rptrAddrSearchEntry,
       "rptrAddrSearchLock": rptrAddrSearchLock,
       "rptrAddrSearchStatus": rptrAddrSearchStatus,
       "rptrAddrSearchAddress": rptrAddrSearchAddress,
       "rptrAddrSearchState": rptrAddrSearchState,
       "rptrAddrSearchGroup": rptrAddrSearchGroup,
       "rptrAddrSearchPort": rptrAddrSearchPort,
       "rptrAddrSearchOwner": rptrAddrSearchOwner,
       "rptrAddrTrackGroupInfo": rptrAddrTrackGroupInfo,
       "rptrAddrTrackPortInfo": rptrAddrTrackPortInfo,
       "rptrAddrTrackTable": rptrAddrTrackTable,
       "rptrAddrTrackEntry": rptrAddrTrackEntry,
       "rptrAddrTrackGroupIndex": rptrAddrTrackGroupIndex,
       "rptrAddrTrackPortIndex": rptrAddrTrackPortIndex,
       "rptrAddrTrackLastSourceAddress": rptrAddrTrackLastSourceAddress,
       "rptrAddrTrackSourceAddrChanges": rptrAddrTrackSourceAddrChanges,
       "rptrAddrTrackNewLastSrcAddress": rptrAddrTrackNewLastSrcAddress,
       "rptrAddrTrackCapacity": rptrAddrTrackCapacity,
       "rptrExtAddrTrackTable": rptrExtAddrTrackTable,
       "rptrExtAddrTrackEntry": rptrExtAddrTrackEntry,
       "rptrExtAddrTrackMacIndex": rptrExtAddrTrackMacIndex,
       "rptrExtAddrTrackSourceAddress": rptrExtAddrTrackSourceAddress,
       "rptrTopNPackage": rptrTopNPackage,
       "rptrTopNRptrInfo": rptrTopNRptrInfo,
       "rptrTopNGroupInfo": rptrTopNGroupInfo,
       "rptrTopNPortInfo": rptrTopNPortInfo,
       "rptrTopNPortControlTable": rptrTopNPortControlTable,
       "rptrTopNPortControlEntry": rptrTopNPortControlEntry,
       "rptrTopNPortControlIndex": rptrTopNPortControlIndex,
       "rptrTopNPortRepeaterId": rptrTopNPortRepeaterId,
       "rptrTopNPortRateBase": rptrTopNPortRateBase,
       "rptrTopNPortTimeRemaining": rptrTopNPortTimeRemaining,
       "rptrTopNPortDuration": rptrTopNPortDuration,
       "rptrTopNPortRequestedSize": rptrTopNPortRequestedSize,
       "rptrTopNPortGrantedSize": rptrTopNPortGrantedSize,
       "rptrTopNPortStartTime": rptrTopNPortStartTime,
       "rptrTopNPortOwner": rptrTopNPortOwner,
       "rptrTopNPortRowStatus": rptrTopNPortRowStatus,
       "rptrTopNPortTable": rptrTopNPortTable,
       "rptrTopNPortEntry": rptrTopNPortEntry,
       "rptrTopNPortIndex": rptrTopNPortIndex,
       "rptrTopNPortGroupIndex": rptrTopNPortGroupIndex,
       "rptrTopNPortPortIndex": rptrTopNPortPortIndex,
       "rptrTopNPortRate": rptrTopNPortRate,
       "snmpRptrMod": snmpRptrMod,
       "snmpRptrModConf": snmpRptrModConf,
       "snmpRptrModCompls": snmpRptrModCompls,
       "snmpRptrModComplRFC1368": snmpRptrModComplRFC1368,
       "snmpRptrModComplRFC1516": snmpRptrModComplRFC1516,
       "snmpRptrModCompl": snmpRptrModCompl,
       "snmpRptrModObjGrps": snmpRptrModObjGrps,
       "snmpRptrGrpBasic1516": snmpRptrGrpBasic1516,
       "snmpRptrGrpMonitor1516": snmpRptrGrpMonitor1516,
       "snmpRptrGrpAddrTrack1368": snmpRptrGrpAddrTrack1368,
       "snmpRptrGrpAddrTrack1516": snmpRptrGrpAddrTrack1516,
       "snmpRptrGrpBasic": snmpRptrGrpBasic,
       "snmpRptrGrpMonitor": snmpRptrGrpMonitor,
       "snmpRptrGrpMonitor100": snmpRptrGrpMonitor100,
       "snmpRptrGrpMonitor100w64": snmpRptrGrpMonitor100w64,
       "snmpRptrGrpAddrTrack": snmpRptrGrpAddrTrack,
       "snmpRptrGrpExtAddrTrack": snmpRptrGrpExtAddrTrack,
       "snmpRptrGrpRptrAddrSearch": snmpRptrGrpRptrAddrSearch,
       "snmpRptrGrpTopNPort": snmpRptrGrpTopNPort,
       "snmpRptrModNotGrps": snmpRptrModNotGrps}
)
