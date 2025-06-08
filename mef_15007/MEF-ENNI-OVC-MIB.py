# SNMP MIB module (MEF-ENNI-OVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/mef_15007/MEF-ENNI-OVC-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:23:56 2025
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

(EntityAdminState,
 EntityOperState) = mibBuilder.importSymbols(
    "ENTITY-STATE-TC-MIB",
    "EntityAdminState",
    "EntityOperState")

(IEEE8021PriorityValue,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021PriorityValue")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(MefServiceDeliveryType,
 MefServiceListType,
 MefServicePreservationType) = mibBuilder.importSymbols(
    "MEF-UNI-EVC-MIB",
    "MefServiceDeliveryType",
    "MefServiceListType",
    "MefServicePreservationType")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 enterprises,
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
    "enterprises",
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


# MODULE-IDENTITY

mefEnniOvcMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3)
)
if mibBuilder.loadTexts:
    mefEnniOvcMib.setRevisions(
        ("2013-07-22 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MefServiceOvcEndPtRoleType(TextualConvention, Integer32):
    status = "current"
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
        *(("root", 1),
          ("leaf", 2),
          ("trunk", 3),
          ("other", 4))
    )



# MIB Managed Objects in the order of their OIDs

_MefServiceEnniOvcObjects_ObjectIdentity = ObjectIdentity
mefServiceEnniOvcObjects = _MefServiceEnniOvcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1)
)
_MefServiceEnniAttributes_ObjectIdentity = ObjectIdentity
mefServiceEnniAttributes = _MefServiceEnniAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 1)
)
_MefServiceEnniCfgTable_Object = MibTable
mefServiceEnniCfgTable = _MefServiceEnniCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mefServiceEnniCfgTable.setStatus("current")
_MefServiceEnniCfgEntry_Object = MibTableRow
mefServiceEnniCfgEntry = _MefServiceEnniCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 1, 1, 1)
)
mefServiceEnniCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mefServiceEnniCfgEntry.setStatus("current")


class _MefServiceEnniCfgIdentifier_Type(DisplayString):
    """Custom type mefServiceEnniCfgIdentifier based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_MefServiceEnniCfgIdentifier_Type.__name__ = "DisplayString"
_MefServiceEnniCfgIdentifier_Object = MibTableColumn
mefServiceEnniCfgIdentifier = _MefServiceEnniCfgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 1, 1, 1, 1),
    _MefServiceEnniCfgIdentifier_Type()
)
mefServiceEnniCfgIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceEnniCfgIdentifier.setStatus("current")


class _MefServiceEnniCfgNumberLinks_Type(Unsigned32):
    """Custom type mefServiceEnniCfgNumberLinks based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MefServiceEnniCfgNumberLinks_Type.__name__ = "Unsigned32"
_MefServiceEnniCfgNumberLinks_Object = MibTableColumn
mefServiceEnniCfgNumberLinks = _MefServiceEnniCfgNumberLinks_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 1, 1, 1, 2),
    _MefServiceEnniCfgNumberLinks_Type()
)
mefServiceEnniCfgNumberLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceEnniCfgNumberLinks.setStatus("current")


class _MefServiceEnniCfgProtection_Type(Integer32):
    """Custom type mefServiceEnniCfgProtection based on Integer32"""
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
          ("linkAggregation", 2),
          ("other", 3))
    )


_MefServiceEnniCfgProtection_Type.__name__ = "Integer32"
_MefServiceEnniCfgProtection_Object = MibTableColumn
mefServiceEnniCfgProtection = _MefServiceEnniCfgProtection_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 1, 1, 1, 3),
    _MefServiceEnniCfgProtection_Type()
)
mefServiceEnniCfgProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceEnniCfgProtection.setStatus("current")


class _MefServiceEnniCfgMaxNumberOvcEndPts_Type(Unsigned32):
    """Custom type mefServiceEnniCfgMaxNumberOvcEndPts based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_MefServiceEnniCfgMaxNumberOvcEndPts_Type.__name__ = "Unsigned32"
_MefServiceEnniCfgMaxNumberOvcEndPts_Object = MibTableColumn
mefServiceEnniCfgMaxNumberOvcEndPts = _MefServiceEnniCfgMaxNumberOvcEndPts_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 1, 1, 1, 4),
    _MefServiceEnniCfgMaxNumberOvcEndPts_Type()
)
mefServiceEnniCfgMaxNumberOvcEndPts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceEnniCfgMaxNumberOvcEndPts.setStatus("current")


class _MefServiceEnniCfgVuniNextIndex_Type(Unsigned32):
    """Custom type mefServiceEnniCfgVuniNextIndex based on Unsigned32"""
    defaultValue = 1


_MefServiceEnniCfgVuniNextIndex_Type.__name__ = "Unsigned32"
_MefServiceEnniCfgVuniNextIndex_Object = MibTableColumn
mefServiceEnniCfgVuniNextIndex = _MefServiceEnniCfgVuniNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 1, 1, 1, 5),
    _MefServiceEnniCfgVuniNextIndex_Type()
)
mefServiceEnniCfgVuniNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceEnniCfgVuniNextIndex.setStatus("current")
_MefServiceVuniAttributes_ObjectIdentity = ObjectIdentity
mefServiceVuniAttributes = _MefServiceVuniAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 2)
)
_MefServiceVuniCfgTable_Object = MibTable
mefServiceVuniCfgTable = _MefServiceVuniCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mefServiceVuniCfgTable.setStatus("current")
_MefServiceVuniCfgEntry_Object = MibTableRow
mefServiceVuniCfgEntry = _MefServiceVuniCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 2, 1, 1)
)
mefServiceVuniCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "MEF-ENNI-OVC-MIB", "mefServiceVuniCfgIndex"),
)
if mibBuilder.loadTexts:
    mefServiceVuniCfgEntry.setStatus("current")
_MefServiceVuniCfgIndex_Type = Unsigned32
_MefServiceVuniCfgIndex_Object = MibTableColumn
mefServiceVuniCfgIndex = _MefServiceVuniCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 2, 1, 1, 1),
    _MefServiceVuniCfgIndex_Type()
)
mefServiceVuniCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefServiceVuniCfgIndex.setStatus("current")


class _MefServiceVuniCfgIdentifier_Type(DisplayString):
    """Custom type mefServiceVuniCfgIdentifier based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_MefServiceVuniCfgIdentifier_Type.__name__ = "DisplayString"
_MefServiceVuniCfgIdentifier_Object = MibTableColumn
mefServiceVuniCfgIdentifier = _MefServiceVuniCfgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 2, 1, 1, 2),
    _MefServiceVuniCfgIdentifier_Type()
)
mefServiceVuniCfgIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceVuniCfgIdentifier.setStatus("current")


class _MefServiceVuniCfgCeVidUntagged_Type(VlanId):
    """Custom type mefServiceVuniCfgCeVidUntagged based on VlanId"""
    defaultValue = 1


_MefServiceVuniCfgCeVidUntagged_Type.__name__ = "VlanId"
_MefServiceVuniCfgCeVidUntagged_Object = MibTableColumn
mefServiceVuniCfgCeVidUntagged = _MefServiceVuniCfgCeVidUntagged_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 2, 1, 1, 3),
    _MefServiceVuniCfgCeVidUntagged_Type()
)
mefServiceVuniCfgCeVidUntagged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceVuniCfgCeVidUntagged.setStatus("current")


class _MefServiceVuniCfgCePriorityUntagged_Type(IEEE8021PriorityValue):
    """Custom type mefServiceVuniCfgCePriorityUntagged based on IEEE8021PriorityValue"""
    defaultValue = 0


_MefServiceVuniCfgCePriorityUntagged_Type.__name__ = "IEEE8021PriorityValue"
_MefServiceVuniCfgCePriorityUntagged_Object = MibTableColumn
mefServiceVuniCfgCePriorityUntagged = _MefServiceVuniCfgCePriorityUntagged_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 2, 1, 1, 4),
    _MefServiceVuniCfgCePriorityUntagged_Type()
)
mefServiceVuniCfgCePriorityUntagged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceVuniCfgCePriorityUntagged.setStatus("current")


class _MefServiceVuniCfgSvlanMap_Type(MefServiceListType):
    """Custom type mefServiceVuniCfgSvlanMap based on MefServiceListType"""
    defaultValue = OctetString("1")


_MefServiceVuniCfgSvlanMap_Type.__name__ = "MefServiceListType"
_MefServiceVuniCfgSvlanMap_Object = MibTableColumn
mefServiceVuniCfgSvlanMap = _MefServiceVuniCfgSvlanMap_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 2, 1, 1, 5),
    _MefServiceVuniCfgSvlanMap_Type()
)
mefServiceVuniCfgSvlanMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceVuniCfgSvlanMap.setStatus("current")


class _MefServiceVuniCfgMaxNumberOvcEndPoints_Type(Unsigned32):
    """Custom type mefServiceVuniCfgMaxNumberOvcEndPoints based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MefServiceVuniCfgMaxNumberOvcEndPoints_Type.__name__ = "Unsigned32"
_MefServiceVuniCfgMaxNumberOvcEndPoints_Object = MibTableColumn
mefServiceVuniCfgMaxNumberOvcEndPoints = _MefServiceVuniCfgMaxNumberOvcEndPoints_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 2, 1, 1, 6),
    _MefServiceVuniCfgMaxNumberOvcEndPoints_Type()
)
mefServiceVuniCfgMaxNumberOvcEndPoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceVuniCfgMaxNumberOvcEndPoints.setStatus("current")


class _MefServiceVuniCfgIngressBwpGrpIndex_Type(Unsigned32):
    """Custom type mefServiceVuniCfgIngressBwpGrpIndex based on Unsigned32"""
    defaultValue = 0


_MefServiceVuniCfgIngressBwpGrpIndex_Type.__name__ = "Unsigned32"
_MefServiceVuniCfgIngressBwpGrpIndex_Object = MibTableColumn
mefServiceVuniCfgIngressBwpGrpIndex = _MefServiceVuniCfgIngressBwpGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 2, 1, 1, 7),
    _MefServiceVuniCfgIngressBwpGrpIndex_Type()
)
mefServiceVuniCfgIngressBwpGrpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceVuniCfgIngressBwpGrpIndex.setStatus("current")


class _MefServiceVuniCfgEgressBwpGrpIndex_Type(Unsigned32):
    """Custom type mefServiceVuniCfgEgressBwpGrpIndex based on Unsigned32"""
    defaultValue = 0


_MefServiceVuniCfgEgressBwpGrpIndex_Type.__name__ = "Unsigned32"
_MefServiceVuniCfgEgressBwpGrpIndex_Object = MibTableColumn
mefServiceVuniCfgEgressBwpGrpIndex = _MefServiceVuniCfgEgressBwpGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 2, 1, 1, 8),
    _MefServiceVuniCfgEgressBwpGrpIndex_Type()
)
mefServiceVuniCfgEgressBwpGrpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceVuniCfgEgressBwpGrpIndex.setStatus("current")


class _MefServiceVuniCfgL2cpGrpIndex_Type(Unsigned32):
    """Custom type mefServiceVuniCfgL2cpGrpIndex based on Unsigned32"""
    defaultValue = 0


_MefServiceVuniCfgL2cpGrpIndex_Type.__name__ = "Unsigned32"
_MefServiceVuniCfgL2cpGrpIndex_Object = MibTableColumn
mefServiceVuniCfgL2cpGrpIndex = _MefServiceVuniCfgL2cpGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 2, 1, 1, 9),
    _MefServiceVuniCfgL2cpGrpIndex_Type()
)
mefServiceVuniCfgL2cpGrpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceVuniCfgL2cpGrpIndex.setStatus("current")
_MefServiceVuniCfgRowStatus_Type = RowStatus
_MefServiceVuniCfgRowStatus_Object = MibTableColumn
mefServiceVuniCfgRowStatus = _MefServiceVuniCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 2, 1, 1, 10),
    _MefServiceVuniCfgRowStatus_Type()
)
mefServiceVuniCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceVuniCfgRowStatus.setStatus("current")
_MefServiceOvcAttributes_ObjectIdentity = ObjectIdentity
mefServiceOvcAttributes = _MefServiceOvcAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3)
)


class _MefServiceOvcNextIndex_Type(Unsigned32):
    """Custom type mefServiceOvcNextIndex based on Unsigned32"""
    defaultValue = 1


_MefServiceOvcNextIndex_Type.__name__ = "Unsigned32"
_MefServiceOvcNextIndex_Object = MibScalar
mefServiceOvcNextIndex = _MefServiceOvcNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 1),
    _MefServiceOvcNextIndex_Type()
)
mefServiceOvcNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceOvcNextIndex.setStatus("current")
_MefServiceOvcCfgTable_Object = MibTable
mefServiceOvcCfgTable = _MefServiceOvcCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    mefServiceOvcCfgTable.setStatus("current")
_MefServiceOvcCfgEntry_Object = MibTableRow
mefServiceOvcCfgEntry = _MefServiceOvcCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 2, 1)
)
mefServiceOvcCfgEntry.setIndexNames(
    (0, "MEF-ENNI-OVC-MIB", "mefServiceOvcCfgIndex"),
)
if mibBuilder.loadTexts:
    mefServiceOvcCfgEntry.setStatus("current")
_MefServiceOvcCfgIndex_Type = Unsigned32
_MefServiceOvcCfgIndex_Object = MibTableColumn
mefServiceOvcCfgIndex = _MefServiceOvcCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 2, 1, 1),
    _MefServiceOvcCfgIndex_Type()
)
mefServiceOvcCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefServiceOvcCfgIndex.setStatus("current")


class _MefServiceOvcCfgIdentifier_Type(DisplayString):
    """Custom type mefServiceOvcCfgIdentifier based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_MefServiceOvcCfgIdentifier_Type.__name__ = "DisplayString"
_MefServiceOvcCfgIdentifier_Object = MibTableColumn
mefServiceOvcCfgIdentifier = _MefServiceOvcCfgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 2, 1, 2),
    _MefServiceOvcCfgIdentifier_Type()
)
mefServiceOvcCfgIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceOvcCfgIdentifier.setStatus("current")


class _MefServiceOvcCfgServiceType_Type(Integer32):
    """Custom type mefServiceOvcCfgServiceType based on Integer32"""
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
        *(("pointToPoint", 1),
          ("multipointToMultipoint", 2),
          ("rootedMultipoint", 3))
    )


_MefServiceOvcCfgServiceType_Type.__name__ = "Integer32"
_MefServiceOvcCfgServiceType_Object = MibTableColumn
mefServiceOvcCfgServiceType = _MefServiceOvcCfgServiceType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 2, 1, 3),
    _MefServiceOvcCfgServiceType_Type()
)
mefServiceOvcCfgServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceOvcCfgServiceType.setStatus("current")


class _MefServiceOvcCfgMtuSize_Type(Unsigned32):
    """Custom type mefServiceOvcCfgMtuSize based on Unsigned32"""
    defaultValue = 1522

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1522, 16384),
    )


_MefServiceOvcCfgMtuSize_Type.__name__ = "Unsigned32"
_MefServiceOvcCfgMtuSize_Object = MibTableColumn
mefServiceOvcCfgMtuSize = _MefServiceOvcCfgMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 2, 1, 4),
    _MefServiceOvcCfgMtuSize_Type()
)
mefServiceOvcCfgMtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceOvcCfgMtuSize.setStatus("current")
if mibBuilder.loadTexts:
    mefServiceOvcCfgMtuSize.setUnits("octets")


class _MefServiceOvcCfgCevlanIdPreservation_Type(MefServicePreservationType):
    """Custom type mefServiceOvcCfgCevlanIdPreservation based on MefServicePreservationType"""
    defaultValue = 1


_MefServiceOvcCfgCevlanIdPreservation_Type.__name__ = "MefServicePreservationType"
_MefServiceOvcCfgCevlanIdPreservation_Object = MibTableColumn
mefServiceOvcCfgCevlanIdPreservation = _MefServiceOvcCfgCevlanIdPreservation_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 2, 1, 5),
    _MefServiceOvcCfgCevlanIdPreservation_Type()
)
mefServiceOvcCfgCevlanIdPreservation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceOvcCfgCevlanIdPreservation.setStatus("current")


class _MefServiceOvcCfgCevlanCosPreservation_Type(MefServicePreservationType):
    """Custom type mefServiceOvcCfgCevlanCosPreservation based on MefServicePreservationType"""
    defaultValue = 1


_MefServiceOvcCfgCevlanCosPreservation_Type.__name__ = "MefServicePreservationType"
_MefServiceOvcCfgCevlanCosPreservation_Object = MibTableColumn
mefServiceOvcCfgCevlanCosPreservation = _MefServiceOvcCfgCevlanCosPreservation_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 2, 1, 6),
    _MefServiceOvcCfgCevlanCosPreservation_Type()
)
mefServiceOvcCfgCevlanCosPreservation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceOvcCfgCevlanCosPreservation.setStatus("current")


class _MefServiceOvcCfgSvlanIdPreservation_Type(MefServicePreservationType):
    """Custom type mefServiceOvcCfgSvlanIdPreservation based on MefServicePreservationType"""
    defaultValue = 1


_MefServiceOvcCfgSvlanIdPreservation_Type.__name__ = "MefServicePreservationType"
_MefServiceOvcCfgSvlanIdPreservation_Object = MibTableColumn
mefServiceOvcCfgSvlanIdPreservation = _MefServiceOvcCfgSvlanIdPreservation_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 2, 1, 7),
    _MefServiceOvcCfgSvlanIdPreservation_Type()
)
mefServiceOvcCfgSvlanIdPreservation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceOvcCfgSvlanIdPreservation.setStatus("current")


class _MefServiceOvcCfgSvlanCosPreservation_Type(MefServicePreservationType):
    """Custom type mefServiceOvcCfgSvlanCosPreservation based on MefServicePreservationType"""
    defaultValue = 1


_MefServiceOvcCfgSvlanCosPreservation_Type.__name__ = "MefServicePreservationType"
_MefServiceOvcCfgSvlanCosPreservation_Object = MibTableColumn
mefServiceOvcCfgSvlanCosPreservation = _MefServiceOvcCfgSvlanCosPreservation_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 2, 1, 8),
    _MefServiceOvcCfgSvlanCosPreservation_Type()
)
mefServiceOvcCfgSvlanCosPreservation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceOvcCfgSvlanCosPreservation.setStatus("current")


class _MefServiceOvcCfgColorForwarding_Type(Integer32):
    """Custom type mefServiceOvcCfgColorForwarding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("colorFwdYes", 1),
          ("colorFwdNo", 2))
    )


_MefServiceOvcCfgColorForwarding_Type.__name__ = "Integer32"
_MefServiceOvcCfgColorForwarding_Object = MibTableColumn
mefServiceOvcCfgColorForwarding = _MefServiceOvcCfgColorForwarding_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 2, 1, 9),
    _MefServiceOvcCfgColorForwarding_Type()
)
mefServiceOvcCfgColorForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceOvcCfgColorForwarding.setStatus("current")


class _MefServiceOvcCfgColorIndicator_Type(Integer32):
    """Custom type mefServiceOvcCfgColorIndicator based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("colorIndicatorPcp", 1),
          ("colorIndicatorDei", 2))
    )


_MefServiceOvcCfgColorIndicator_Type.__name__ = "Integer32"
_MefServiceOvcCfgColorIndicator_Object = MibTableColumn
mefServiceOvcCfgColorIndicator = _MefServiceOvcCfgColorIndicator_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 2, 1, 10),
    _MefServiceOvcCfgColorIndicator_Type()
)
mefServiceOvcCfgColorIndicator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceOvcCfgColorIndicator.setStatus("current")


class _MefServiceOvcCfgUnicastDelivery_Type(MefServiceDeliveryType):
    """Custom type mefServiceOvcCfgUnicastDelivery based on MefServiceDeliveryType"""
    defaultValue = 2


_MefServiceOvcCfgUnicastDelivery_Type.__name__ = "MefServiceDeliveryType"
_MefServiceOvcCfgUnicastDelivery_Object = MibTableColumn
mefServiceOvcCfgUnicastDelivery = _MefServiceOvcCfgUnicastDelivery_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 2, 1, 11),
    _MefServiceOvcCfgUnicastDelivery_Type()
)
mefServiceOvcCfgUnicastDelivery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceOvcCfgUnicastDelivery.setStatus("current")


class _MefServiceOvcCfgMulticastDelivery_Type(MefServiceDeliveryType):
    """Custom type mefServiceOvcCfgMulticastDelivery based on MefServiceDeliveryType"""
    defaultValue = 2


_MefServiceOvcCfgMulticastDelivery_Type.__name__ = "MefServiceDeliveryType"
_MefServiceOvcCfgMulticastDelivery_Object = MibTableColumn
mefServiceOvcCfgMulticastDelivery = _MefServiceOvcCfgMulticastDelivery_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 2, 1, 12),
    _MefServiceOvcCfgMulticastDelivery_Type()
)
mefServiceOvcCfgMulticastDelivery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceOvcCfgMulticastDelivery.setStatus("current")


class _MefServiceOvcCfgBroadcastDelivery_Type(MefServiceDeliveryType):
    """Custom type mefServiceOvcCfgBroadcastDelivery based on MefServiceDeliveryType"""
    defaultValue = 2


_MefServiceOvcCfgBroadcastDelivery_Type.__name__ = "MefServiceDeliveryType"
_MefServiceOvcCfgBroadcastDelivery_Object = MibTableColumn
mefServiceOvcCfgBroadcastDelivery = _MefServiceOvcCfgBroadcastDelivery_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 2, 1, 13),
    _MefServiceOvcCfgBroadcastDelivery_Type()
)
mefServiceOvcCfgBroadcastDelivery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceOvcCfgBroadcastDelivery.setStatus("current")


class _MefServiceOvcCfgL2cpGrpIndex_Type(Unsigned32):
    """Custom type mefServiceOvcCfgL2cpGrpIndex based on Unsigned32"""
    defaultValue = 0


_MefServiceOvcCfgL2cpGrpIndex_Type.__name__ = "Unsigned32"
_MefServiceOvcCfgL2cpGrpIndex_Object = MibTableColumn
mefServiceOvcCfgL2cpGrpIndex = _MefServiceOvcCfgL2cpGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 2, 1, 14),
    _MefServiceOvcCfgL2cpGrpIndex_Type()
)
mefServiceOvcCfgL2cpGrpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceOvcCfgL2cpGrpIndex.setStatus("current")


class _MefServiceOvcCfgAdminState_Type(EntityAdminState):
    """Custom type mefServiceOvcCfgAdminState based on EntityAdminState"""
    defaultValue = 4


_MefServiceOvcCfgAdminState_Type.__name__ = "EntityAdminState"
_MefServiceOvcCfgAdminState_Object = MibTableColumn
mefServiceOvcCfgAdminState = _MefServiceOvcCfgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 2, 1, 15),
    _MefServiceOvcCfgAdminState_Type()
)
mefServiceOvcCfgAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceOvcCfgAdminState.setStatus("current")
_MefServiceOvcCfgRowStatus_Type = RowStatus
_MefServiceOvcCfgRowStatus_Object = MibTableColumn
mefServiceOvcCfgRowStatus = _MefServiceOvcCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 2, 1, 16),
    _MefServiceOvcCfgRowStatus_Type()
)
mefServiceOvcCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceOvcCfgRowStatus.setStatus("current")
_MefServiceOvcStatusTable_Object = MibTable
mefServiceOvcStatusTable = _MefServiceOvcStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 4)
)
if mibBuilder.loadTexts:
    mefServiceOvcStatusTable.setStatus("current")
_MefServiceOvcStatusEntry_Object = MibTableRow
mefServiceOvcStatusEntry = _MefServiceOvcStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 4, 1)
)
mefServiceOvcStatusEntry.setIndexNames(
    (0, "MEF-ENNI-OVC-MIB", "mefServiceOvcCfgIndex"),
)
if mibBuilder.loadTexts:
    mefServiceOvcStatusEntry.setStatus("current")


class _MefServiceOvcStatusMaxMtuSize_Type(Unsigned32):
    """Custom type mefServiceOvcStatusMaxMtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1526, 16384),
    )


_MefServiceOvcStatusMaxMtuSize_Type.__name__ = "Unsigned32"
_MefServiceOvcStatusMaxMtuSize_Object = MibTableColumn
mefServiceOvcStatusMaxMtuSize = _MefServiceOvcStatusMaxMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 4, 1, 1),
    _MefServiceOvcStatusMaxMtuSize_Type()
)
mefServiceOvcStatusMaxMtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceOvcStatusMaxMtuSize.setStatus("current")
if mibBuilder.loadTexts:
    mefServiceOvcStatusMaxMtuSize.setUnits("octets")


class _MefServiceOvcStatusMaxNumEnniOvcEndPt_Type(Unsigned32):
    """Custom type mefServiceOvcStatusMaxNumEnniOvcEndPt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 16384),
    )


_MefServiceOvcStatusMaxNumEnniOvcEndPt_Type.__name__ = "Unsigned32"
_MefServiceOvcStatusMaxNumEnniOvcEndPt_Object = MibTableColumn
mefServiceOvcStatusMaxNumEnniOvcEndPt = _MefServiceOvcStatusMaxNumEnniOvcEndPt_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 4, 1, 2),
    _MefServiceOvcStatusMaxNumEnniOvcEndPt_Type()
)
mefServiceOvcStatusMaxNumEnniOvcEndPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceOvcStatusMaxNumEnniOvcEndPt.setStatus("current")


class _MefServiceOvcStatusMaxNumVuniOvcEndPt_Type(Unsigned32):
    """Custom type mefServiceOvcStatusMaxNumVuniOvcEndPt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 16384),
    )


_MefServiceOvcStatusMaxNumVuniOvcEndPt_Type.__name__ = "Unsigned32"
_MefServiceOvcStatusMaxNumVuniOvcEndPt_Object = MibTableColumn
mefServiceOvcStatusMaxNumVuniOvcEndPt = _MefServiceOvcStatusMaxNumVuniOvcEndPt_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 4, 1, 3),
    _MefServiceOvcStatusMaxNumVuniOvcEndPt_Type()
)
mefServiceOvcStatusMaxNumVuniOvcEndPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceOvcStatusMaxNumVuniOvcEndPt.setStatus("current")
_MefServiceOvcStatusOperationalState_Type = EntityOperState
_MefServiceOvcStatusOperationalState_Object = MibTableColumn
mefServiceOvcStatusOperationalState = _MefServiceOvcStatusOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 4, 1, 4),
    _MefServiceOvcStatusOperationalState_Type()
)
mefServiceOvcStatusOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceOvcStatusOperationalState.setStatus("current")
_MefServiceOvcEndPtPerEnniCfgTable_Object = MibTable
mefServiceOvcEndPtPerEnniCfgTable = _MefServiceOvcEndPtPerEnniCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 5)
)
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerEnniCfgTable.setStatus("current")
_MefServiceOvcEndPtPerEnniCfgEntry_Object = MibTableRow
mefServiceOvcEndPtPerEnniCfgEntry = _MefServiceOvcEndPtPerEnniCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 5, 1)
)
mefServiceOvcEndPtPerEnniCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "MEF-ENNI-OVC-MIB", "mefServiceOvcCfgIndex"),
)
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerEnniCfgEntry.setStatus("current")


class _MefServiceOvcEndPtPerEnniCfgIdentifier_Type(DisplayString):
    """Custom type mefServiceOvcEndPtPerEnniCfgIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_MefServiceOvcEndPtPerEnniCfgIdentifier_Type.__name__ = "DisplayString"
_MefServiceOvcEndPtPerEnniCfgIdentifier_Object = MibTableColumn
mefServiceOvcEndPtPerEnniCfgIdentifier = _MefServiceOvcEndPtPerEnniCfgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 5, 1, 1),
    _MefServiceOvcEndPtPerEnniCfgIdentifier_Type()
)
mefServiceOvcEndPtPerEnniCfgIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerEnniCfgIdentifier.setStatus("current")


class _MefServiceOvcEndPtPerEnniCfgRole_Type(MefServiceOvcEndPtRoleType):
    """Custom type mefServiceOvcEndPtPerEnniCfgRole based on MefServiceOvcEndPtRoleType"""
    defaultValue = 1


_MefServiceOvcEndPtPerEnniCfgRole_Type.__name__ = "MefServiceOvcEndPtRoleType"
_MefServiceOvcEndPtPerEnniCfgRole_Object = MibTableColumn
mefServiceOvcEndPtPerEnniCfgRole = _MefServiceOvcEndPtPerEnniCfgRole_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 5, 1, 2),
    _MefServiceOvcEndPtPerEnniCfgRole_Type()
)
mefServiceOvcEndPtPerEnniCfgRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerEnniCfgRole.setStatus("current")


class _MefServiceOvcEndPtPerEnniCfgRootSvlanMap_Type(MefServiceListType):
    """Custom type mefServiceOvcEndPtPerEnniCfgRootSvlanMap based on MefServiceListType"""
    defaultValue = OctetString("")


_MefServiceOvcEndPtPerEnniCfgRootSvlanMap_Type.__name__ = "MefServiceListType"
_MefServiceOvcEndPtPerEnniCfgRootSvlanMap_Object = MibTableColumn
mefServiceOvcEndPtPerEnniCfgRootSvlanMap = _MefServiceOvcEndPtPerEnniCfgRootSvlanMap_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 5, 1, 3),
    _MefServiceOvcEndPtPerEnniCfgRootSvlanMap_Type()
)
mefServiceOvcEndPtPerEnniCfgRootSvlanMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerEnniCfgRootSvlanMap.setStatus("current")


class _MefServiceOvcEndPtPerEnniCfgLeafSvlanMap_Type(MefServiceListType):
    """Custom type mefServiceOvcEndPtPerEnniCfgLeafSvlanMap based on MefServiceListType"""
    defaultValue = OctetString("")


_MefServiceOvcEndPtPerEnniCfgLeafSvlanMap_Type.__name__ = "MefServiceListType"
_MefServiceOvcEndPtPerEnniCfgLeafSvlanMap_Object = MibTableColumn
mefServiceOvcEndPtPerEnniCfgLeafSvlanMap = _MefServiceOvcEndPtPerEnniCfgLeafSvlanMap_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 5, 1, 4),
    _MefServiceOvcEndPtPerEnniCfgLeafSvlanMap_Type()
)
mefServiceOvcEndPtPerEnniCfgLeafSvlanMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerEnniCfgLeafSvlanMap.setStatus("current")


class _MefServiceOvcEndPtPerEnniCfgIngressBwpGrpIndex_Type(Unsigned32):
    """Custom type mefServiceOvcEndPtPerEnniCfgIngressBwpGrpIndex based on Unsigned32"""
    defaultValue = 0


_MefServiceOvcEndPtPerEnniCfgIngressBwpGrpIndex_Type.__name__ = "Unsigned32"
_MefServiceOvcEndPtPerEnniCfgIngressBwpGrpIndex_Object = MibTableColumn
mefServiceOvcEndPtPerEnniCfgIngressBwpGrpIndex = _MefServiceOvcEndPtPerEnniCfgIngressBwpGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 5, 1, 5),
    _MefServiceOvcEndPtPerEnniCfgIngressBwpGrpIndex_Type()
)
mefServiceOvcEndPtPerEnniCfgIngressBwpGrpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerEnniCfgIngressBwpGrpIndex.setStatus("current")


class _MefServiceOvcEndPtPerEnniCfgEgressBwpGrpIndex_Type(Unsigned32):
    """Custom type mefServiceOvcEndPtPerEnniCfgEgressBwpGrpIndex based on Unsigned32"""
    defaultValue = 0


_MefServiceOvcEndPtPerEnniCfgEgressBwpGrpIndex_Type.__name__ = "Unsigned32"
_MefServiceOvcEndPtPerEnniCfgEgressBwpGrpIndex_Object = MibTableColumn
mefServiceOvcEndPtPerEnniCfgEgressBwpGrpIndex = _MefServiceOvcEndPtPerEnniCfgEgressBwpGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 5, 1, 6),
    _MefServiceOvcEndPtPerEnniCfgEgressBwpGrpIndex_Type()
)
mefServiceOvcEndPtPerEnniCfgEgressBwpGrpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerEnniCfgEgressBwpGrpIndex.setStatus("current")
_MefServiceOvcEndPtPerEnniCfgRowStatus_Type = RowStatus
_MefServiceOvcEndPtPerEnniCfgRowStatus_Object = MibTableColumn
mefServiceOvcEndPtPerEnniCfgRowStatus = _MefServiceOvcEndPtPerEnniCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 5, 1, 7),
    _MefServiceOvcEndPtPerEnniCfgRowStatus_Type()
)
mefServiceOvcEndPtPerEnniCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerEnniCfgRowStatus.setStatus("current")
_MefServiceOvcEndPtPerUniCfgTable_Object = MibTable
mefServiceOvcEndPtPerUniCfgTable = _MefServiceOvcEndPtPerUniCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 6)
)
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerUniCfgTable.setStatus("current")
_MefServiceOvcEndPtPerUniCfgEntry_Object = MibTableRow
mefServiceOvcEndPtPerUniCfgEntry = _MefServiceOvcEndPtPerUniCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 6, 1)
)
mefServiceOvcEndPtPerUniCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "MEF-ENNI-OVC-MIB", "mefServiceOvcCfgIndex"),
)
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerUniCfgEntry.setStatus("current")


class _MefServiceOvcEndPtPerUniCfgIdentifier_Type(DisplayString):
    """Custom type mefServiceOvcEndPtPerUniCfgIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 90),
    )


_MefServiceOvcEndPtPerUniCfgIdentifier_Type.__name__ = "DisplayString"
_MefServiceOvcEndPtPerUniCfgIdentifier_Object = MibTableColumn
mefServiceOvcEndPtPerUniCfgIdentifier = _MefServiceOvcEndPtPerUniCfgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 6, 1, 1),
    _MefServiceOvcEndPtPerUniCfgIdentifier_Type()
)
mefServiceOvcEndPtPerUniCfgIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerUniCfgIdentifier.setStatus("current")


class _MefServiceOvcEndPtPerUniCfgRole_Type(MefServiceOvcEndPtRoleType):
    """Custom type mefServiceOvcEndPtPerUniCfgRole based on MefServiceOvcEndPtRoleType"""
    defaultValue = 1


_MefServiceOvcEndPtPerUniCfgRole_Type.__name__ = "MefServiceOvcEndPtRoleType"
_MefServiceOvcEndPtPerUniCfgRole_Object = MibTableColumn
mefServiceOvcEndPtPerUniCfgRole = _MefServiceOvcEndPtPerUniCfgRole_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 6, 1, 2),
    _MefServiceOvcEndPtPerUniCfgRole_Type()
)
mefServiceOvcEndPtPerUniCfgRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerUniCfgRole.setStatus("current")


class _MefServiceOvcEndPtPerUniCfgCeVlanMap_Type(MefServiceListType):
    """Custom type mefServiceOvcEndPtPerUniCfgCeVlanMap based on MefServiceListType"""
    defaultValue = OctetString("1:4095")


_MefServiceOvcEndPtPerUniCfgCeVlanMap_Type.__name__ = "MefServiceListType"
_MefServiceOvcEndPtPerUniCfgCeVlanMap_Object = MibTableColumn
mefServiceOvcEndPtPerUniCfgCeVlanMap = _MefServiceOvcEndPtPerUniCfgCeVlanMap_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 6, 1, 3),
    _MefServiceOvcEndPtPerUniCfgCeVlanMap_Type()
)
mefServiceOvcEndPtPerUniCfgCeVlanMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerUniCfgCeVlanMap.setStatus("current")


class _MefServiceOvcEndPtPerUniCfgIngressBwpGrpIndex_Type(Unsigned32):
    """Custom type mefServiceOvcEndPtPerUniCfgIngressBwpGrpIndex based on Unsigned32"""
    defaultValue = 0


_MefServiceOvcEndPtPerUniCfgIngressBwpGrpIndex_Type.__name__ = "Unsigned32"
_MefServiceOvcEndPtPerUniCfgIngressBwpGrpIndex_Object = MibTableColumn
mefServiceOvcEndPtPerUniCfgIngressBwpGrpIndex = _MefServiceOvcEndPtPerUniCfgIngressBwpGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 6, 1, 4),
    _MefServiceOvcEndPtPerUniCfgIngressBwpGrpIndex_Type()
)
mefServiceOvcEndPtPerUniCfgIngressBwpGrpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerUniCfgIngressBwpGrpIndex.setStatus("current")


class _MefServiceOvcEndPtPerUniCfgEgressBwpGrpIndex_Type(Unsigned32):
    """Custom type mefServiceOvcEndPtPerUniCfgEgressBwpGrpIndex based on Unsigned32"""
    defaultValue = 0


_MefServiceOvcEndPtPerUniCfgEgressBwpGrpIndex_Type.__name__ = "Unsigned32"
_MefServiceOvcEndPtPerUniCfgEgressBwpGrpIndex_Object = MibTableColumn
mefServiceOvcEndPtPerUniCfgEgressBwpGrpIndex = _MefServiceOvcEndPtPerUniCfgEgressBwpGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 6, 1, 5),
    _MefServiceOvcEndPtPerUniCfgEgressBwpGrpIndex_Type()
)
mefServiceOvcEndPtPerUniCfgEgressBwpGrpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerUniCfgEgressBwpGrpIndex.setStatus("current")
_MefServiceOvcEndPtPerUniCfgRowStatus_Type = RowStatus
_MefServiceOvcEndPtPerUniCfgRowStatus_Object = MibTableColumn
mefServiceOvcEndPtPerUniCfgRowStatus = _MefServiceOvcEndPtPerUniCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 6, 1, 6),
    _MefServiceOvcEndPtPerUniCfgRowStatus_Type()
)
mefServiceOvcEndPtPerUniCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerUniCfgRowStatus.setStatus("current")
_MefServiceOvcEndPtPerVuniCfgTable_Object = MibTable
mefServiceOvcEndPtPerVuniCfgTable = _MefServiceOvcEndPtPerVuniCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 7)
)
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerVuniCfgTable.setStatus("current")
_MefServiceOvcEndPtPerVuniCfgEntry_Object = MibTableRow
mefServiceOvcEndPtPerVuniCfgEntry = _MefServiceOvcEndPtPerVuniCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 7, 1)
)
mefServiceOvcEndPtPerVuniCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "MEF-ENNI-OVC-MIB", "mefServiceVuniCfgIndex"),
    (0, "MEF-ENNI-OVC-MIB", "mefServiceOvcCfgIndex"),
)
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerVuniCfgEntry.setStatus("current")


class _MefServiceOvcEndPtPerVuniCfgIdentifier_Type(DisplayString):
    """Custom type mefServiceOvcEndPtPerVuniCfgIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 90),
    )


_MefServiceOvcEndPtPerVuniCfgIdentifier_Type.__name__ = "DisplayString"
_MefServiceOvcEndPtPerVuniCfgIdentifier_Object = MibTableColumn
mefServiceOvcEndPtPerVuniCfgIdentifier = _MefServiceOvcEndPtPerVuniCfgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 7, 1, 1),
    _MefServiceOvcEndPtPerVuniCfgIdentifier_Type()
)
mefServiceOvcEndPtPerVuniCfgIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerVuniCfgIdentifier.setStatus("current")


class _MefServiceOvcEndPtPerVuniCfgRole_Type(MefServiceOvcEndPtRoleType):
    """Custom type mefServiceOvcEndPtPerVuniCfgRole based on MefServiceOvcEndPtRoleType"""
    defaultValue = 1


_MefServiceOvcEndPtPerVuniCfgRole_Type.__name__ = "MefServiceOvcEndPtRoleType"
_MefServiceOvcEndPtPerVuniCfgRole_Object = MibTableColumn
mefServiceOvcEndPtPerVuniCfgRole = _MefServiceOvcEndPtPerVuniCfgRole_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 7, 1, 2),
    _MefServiceOvcEndPtPerVuniCfgRole_Type()
)
mefServiceOvcEndPtPerVuniCfgRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerVuniCfgRole.setStatus("current")


class _MefServiceOvcEndPtPerVuniCfgCeVlanMap_Type(MefServiceListType):
    """Custom type mefServiceOvcEndPtPerVuniCfgCeVlanMap based on MefServiceListType"""
    defaultValue = OctetString("1:4095")


_MefServiceOvcEndPtPerVuniCfgCeVlanMap_Type.__name__ = "MefServiceListType"
_MefServiceOvcEndPtPerVuniCfgCeVlanMap_Object = MibTableColumn
mefServiceOvcEndPtPerVuniCfgCeVlanMap = _MefServiceOvcEndPtPerVuniCfgCeVlanMap_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 7, 1, 3),
    _MefServiceOvcEndPtPerVuniCfgCeVlanMap_Type()
)
mefServiceOvcEndPtPerVuniCfgCeVlanMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerVuniCfgCeVlanMap.setStatus("current")


class _MefServiceOvcEndPtPerVuniCfgIngressBwpGrpIndex_Type(Unsigned32):
    """Custom type mefServiceOvcEndPtPerVuniCfgIngressBwpGrpIndex based on Unsigned32"""
    defaultValue = 0


_MefServiceOvcEndPtPerVuniCfgIngressBwpGrpIndex_Type.__name__ = "Unsigned32"
_MefServiceOvcEndPtPerVuniCfgIngressBwpGrpIndex_Object = MibTableColumn
mefServiceOvcEndPtPerVuniCfgIngressBwpGrpIndex = _MefServiceOvcEndPtPerVuniCfgIngressBwpGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 7, 1, 4),
    _MefServiceOvcEndPtPerVuniCfgIngressBwpGrpIndex_Type()
)
mefServiceOvcEndPtPerVuniCfgIngressBwpGrpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerVuniCfgIngressBwpGrpIndex.setStatus("current")


class _MefServiceOvcEndPtPerVuniCfgEgressBwpGrpIndex_Type(Unsigned32):
    """Custom type mefServiceOvcEndPtPerVuniCfgEgressBwpGrpIndex based on Unsigned32"""
    defaultValue = 0


_MefServiceOvcEndPtPerVuniCfgEgressBwpGrpIndex_Type.__name__ = "Unsigned32"
_MefServiceOvcEndPtPerVuniCfgEgressBwpGrpIndex_Object = MibTableColumn
mefServiceOvcEndPtPerVuniCfgEgressBwpGrpIndex = _MefServiceOvcEndPtPerVuniCfgEgressBwpGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 7, 1, 5),
    _MefServiceOvcEndPtPerVuniCfgEgressBwpGrpIndex_Type()
)
mefServiceOvcEndPtPerVuniCfgEgressBwpGrpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerVuniCfgEgressBwpGrpIndex.setStatus("current")
_MefServiceOvcEndPtPerVuniCfgRowStatus_Type = RowStatus
_MefServiceOvcEndPtPerVuniCfgRowStatus_Object = MibTableColumn
mefServiceOvcEndPtPerVuniCfgRowStatus = _MefServiceOvcEndPtPerVuniCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 1, 3, 7, 1, 6),
    _MefServiceOvcEndPtPerVuniCfgRowStatus_Type()
)
mefServiceOvcEndPtPerVuniCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefServiceOvcEndPtPerVuniCfgRowStatus.setStatus("current")
_MefServiceEnniOvcMibConformance_ObjectIdentity = ObjectIdentity
mefServiceEnniOvcMibConformance = _MefServiceEnniOvcMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 2)
)
_MefServiceEnniOvcMibCompliances_ObjectIdentity = ObjectIdentity
mefServiceEnniOvcMibCompliances = _MefServiceEnniOvcMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 2, 1)
)
_MefServiceEnniOvcMibGroups_ObjectIdentity = ObjectIdentity
mefServiceEnniOvcMibGroups = _MefServiceEnniOvcMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 2, 2)
)

# Managed Objects groups

mefServiceEnniMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 2, 2, 1)
)
mefServiceEnniMandatoryGroup.setObjects(
      *(("MEF-ENNI-OVC-MIB", "mefServiceEnniCfgIdentifier"),
        ("MEF-ENNI-OVC-MIB", "mefServiceEnniCfgNumberLinks"),
        ("MEF-ENNI-OVC-MIB", "mefServiceEnniCfgProtection"),
        ("MEF-ENNI-OVC-MIB", "mefServiceEnniCfgMaxNumberOvcEndPts"),
        ("MEF-ENNI-OVC-MIB", "mefServiceEnniCfgVuniNextIndex"))
)
if mibBuilder.loadTexts:
    mefServiceEnniMandatoryGroup.setStatus("current")

mefServiceVuniOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 2, 2, 2)
)
mefServiceVuniOptionalGroup.setObjects(
      *(("MEF-ENNI-OVC-MIB", "mefServiceVuniCfgIdentifier"),
        ("MEF-ENNI-OVC-MIB", "mefServiceVuniCfgCeVidUntagged"),
        ("MEF-ENNI-OVC-MIB", "mefServiceVuniCfgCePriorityUntagged"),
        ("MEF-ENNI-OVC-MIB", "mefServiceVuniCfgSvlanMap"),
        ("MEF-ENNI-OVC-MIB", "mefServiceVuniCfgMaxNumberOvcEndPoints"),
        ("MEF-ENNI-OVC-MIB", "mefServiceVuniCfgIngressBwpGrpIndex"),
        ("MEF-ENNI-OVC-MIB", "mefServiceVuniCfgEgressBwpGrpIndex"),
        ("MEF-ENNI-OVC-MIB", "mefServiceVuniCfgL2cpGrpIndex"),
        ("MEF-ENNI-OVC-MIB", "mefServiceVuniCfgRowStatus"))
)
if mibBuilder.loadTexts:
    mefServiceVuniOptionalGroup.setStatus("current")

mefServiceOvcMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 2, 2, 3)
)
mefServiceOvcMandatoryGroup.setObjects(
      *(("MEF-ENNI-OVC-MIB", "mefServiceOvcNextIndex"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcCfgIdentifier"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcCfgServiceType"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcCfgMtuSize"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcCfgCevlanIdPreservation"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcCfgCevlanCosPreservation"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcCfgSvlanIdPreservation"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcCfgSvlanCosPreservation"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcCfgColorForwarding"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcCfgColorIndicator"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcCfgUnicastDelivery"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcCfgMulticastDelivery"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcCfgBroadcastDelivery"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcCfgL2cpGrpIndex"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcCfgAdminState"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcCfgRowStatus"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcStatusMaxMtuSize"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcStatusMaxNumEnniOvcEndPt"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcStatusMaxNumVuniOvcEndPt"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcStatusOperationalState"))
)
if mibBuilder.loadTexts:
    mefServiceOvcMandatoryGroup.setStatus("current")

mefServiceOvcPerEndPtPerEnniMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 2, 2, 4)
)
mefServiceOvcPerEndPtPerEnniMandatoryGroup.setObjects(
      *(("MEF-ENNI-OVC-MIB", "mefServiceOvcEndPtPerEnniCfgIdentifier"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcEndPtPerEnniCfgRole"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcEndPtPerEnniCfgRootSvlanMap"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcEndPtPerEnniCfgLeafSvlanMap"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcEndPtPerEnniCfgIngressBwpGrpIndex"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcEndPtPerEnniCfgEgressBwpGrpIndex"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcEndPtPerEnniCfgRowStatus"))
)
if mibBuilder.loadTexts:
    mefServiceOvcPerEndPtPerEnniMandatoryGroup.setStatus("current")

mefServiceOvcPerEndPtPerUniMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 2, 2, 5)
)
mefServiceOvcPerEndPtPerUniMandatoryGroup.setObjects(
      *(("MEF-ENNI-OVC-MIB", "mefServiceOvcEndPtPerUniCfgIdentifier"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcEndPtPerUniCfgRole"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcEndPtPerUniCfgCeVlanMap"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcEndPtPerUniCfgIngressBwpGrpIndex"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcEndPtPerUniCfgEgressBwpGrpIndex"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcEndPtPerUniCfgRowStatus"))
)
if mibBuilder.loadTexts:
    mefServiceOvcPerEndPtPerUniMandatoryGroup.setStatus("current")

mefServiceOvcPerEndPtPerVuniOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 2, 2, 6)
)
mefServiceOvcPerEndPtPerVuniOptionalGroup.setObjects(
      *(("MEF-ENNI-OVC-MIB", "mefServiceOvcEndPtPerVuniCfgIdentifier"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcEndPtPerVuniCfgRole"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcEndPtPerVuniCfgCeVlanMap"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcEndPtPerVuniCfgIngressBwpGrpIndex"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcEndPtPerVuniCfgEgressBwpGrpIndex"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcEndPtPerVuniCfgRowStatus"))
)
if mibBuilder.loadTexts:
    mefServiceOvcPerEndPtPerVuniOptionalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mefServiceEnniOvcMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 15007, 2, 3, 2, 1, 1)
)
mefServiceEnniOvcMibCompliance.setObjects(
      *(("MEF-ENNI-OVC-MIB", "mefServiceEnniMandatoryGroup"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcMandatoryGroup"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcPerEndPtPerEnniMandatoryGroup"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcPerEndPtPerUniMandatoryGroup"),
        ("MEF-ENNI-OVC-MIB", "mefServiceVuniOptionalGroup"),
        ("MEF-ENNI-OVC-MIB", "mefServiceOvcPerEndPtPerVuniOptionalGroup"))
)
if mibBuilder.loadTexts:
    mefServiceEnniOvcMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MEF-ENNI-OVC-MIB",
    **{"MefServiceOvcEndPtRoleType": MefServiceOvcEndPtRoleType,
       "mefEnniOvcMib": mefEnniOvcMib,
       "mefServiceEnniOvcObjects": mefServiceEnniOvcObjects,
       "mefServiceEnniAttributes": mefServiceEnniAttributes,
       "mefServiceEnniCfgTable": mefServiceEnniCfgTable,
       "mefServiceEnniCfgEntry": mefServiceEnniCfgEntry,
       "mefServiceEnniCfgIdentifier": mefServiceEnniCfgIdentifier,
       "mefServiceEnniCfgNumberLinks": mefServiceEnniCfgNumberLinks,
       "mefServiceEnniCfgProtection": mefServiceEnniCfgProtection,
       "mefServiceEnniCfgMaxNumberOvcEndPts": mefServiceEnniCfgMaxNumberOvcEndPts,
       "mefServiceEnniCfgVuniNextIndex": mefServiceEnniCfgVuniNextIndex,
       "mefServiceVuniAttributes": mefServiceVuniAttributes,
       "mefServiceVuniCfgTable": mefServiceVuniCfgTable,
       "mefServiceVuniCfgEntry": mefServiceVuniCfgEntry,
       "mefServiceVuniCfgIndex": mefServiceVuniCfgIndex,
       "mefServiceVuniCfgIdentifier": mefServiceVuniCfgIdentifier,
       "mefServiceVuniCfgCeVidUntagged": mefServiceVuniCfgCeVidUntagged,
       "mefServiceVuniCfgCePriorityUntagged": mefServiceVuniCfgCePriorityUntagged,
       "mefServiceVuniCfgSvlanMap": mefServiceVuniCfgSvlanMap,
       "mefServiceVuniCfgMaxNumberOvcEndPoints": mefServiceVuniCfgMaxNumberOvcEndPoints,
       "mefServiceVuniCfgIngressBwpGrpIndex": mefServiceVuniCfgIngressBwpGrpIndex,
       "mefServiceVuniCfgEgressBwpGrpIndex": mefServiceVuniCfgEgressBwpGrpIndex,
       "mefServiceVuniCfgL2cpGrpIndex": mefServiceVuniCfgL2cpGrpIndex,
       "mefServiceVuniCfgRowStatus": mefServiceVuniCfgRowStatus,
       "mefServiceOvcAttributes": mefServiceOvcAttributes,
       "mefServiceOvcNextIndex": mefServiceOvcNextIndex,
       "mefServiceOvcCfgTable": mefServiceOvcCfgTable,
       "mefServiceOvcCfgEntry": mefServiceOvcCfgEntry,
       "mefServiceOvcCfgIndex": mefServiceOvcCfgIndex,
       "mefServiceOvcCfgIdentifier": mefServiceOvcCfgIdentifier,
       "mefServiceOvcCfgServiceType": mefServiceOvcCfgServiceType,
       "mefServiceOvcCfgMtuSize": mefServiceOvcCfgMtuSize,
       "mefServiceOvcCfgCevlanIdPreservation": mefServiceOvcCfgCevlanIdPreservation,
       "mefServiceOvcCfgCevlanCosPreservation": mefServiceOvcCfgCevlanCosPreservation,
       "mefServiceOvcCfgSvlanIdPreservation": mefServiceOvcCfgSvlanIdPreservation,
       "mefServiceOvcCfgSvlanCosPreservation": mefServiceOvcCfgSvlanCosPreservation,
       "mefServiceOvcCfgColorForwarding": mefServiceOvcCfgColorForwarding,
       "mefServiceOvcCfgColorIndicator": mefServiceOvcCfgColorIndicator,
       "mefServiceOvcCfgUnicastDelivery": mefServiceOvcCfgUnicastDelivery,
       "mefServiceOvcCfgMulticastDelivery": mefServiceOvcCfgMulticastDelivery,
       "mefServiceOvcCfgBroadcastDelivery": mefServiceOvcCfgBroadcastDelivery,
       "mefServiceOvcCfgL2cpGrpIndex": mefServiceOvcCfgL2cpGrpIndex,
       "mefServiceOvcCfgAdminState": mefServiceOvcCfgAdminState,
       "mefServiceOvcCfgRowStatus": mefServiceOvcCfgRowStatus,
       "mefServiceOvcStatusTable": mefServiceOvcStatusTable,
       "mefServiceOvcStatusEntry": mefServiceOvcStatusEntry,
       "mefServiceOvcStatusMaxMtuSize": mefServiceOvcStatusMaxMtuSize,
       "mefServiceOvcStatusMaxNumEnniOvcEndPt": mefServiceOvcStatusMaxNumEnniOvcEndPt,
       "mefServiceOvcStatusMaxNumVuniOvcEndPt": mefServiceOvcStatusMaxNumVuniOvcEndPt,
       "mefServiceOvcStatusOperationalState": mefServiceOvcStatusOperationalState,
       "mefServiceOvcEndPtPerEnniCfgTable": mefServiceOvcEndPtPerEnniCfgTable,
       "mefServiceOvcEndPtPerEnniCfgEntry": mefServiceOvcEndPtPerEnniCfgEntry,
       "mefServiceOvcEndPtPerEnniCfgIdentifier": mefServiceOvcEndPtPerEnniCfgIdentifier,
       "mefServiceOvcEndPtPerEnniCfgRole": mefServiceOvcEndPtPerEnniCfgRole,
       "mefServiceOvcEndPtPerEnniCfgRootSvlanMap": mefServiceOvcEndPtPerEnniCfgRootSvlanMap,
       "mefServiceOvcEndPtPerEnniCfgLeafSvlanMap": mefServiceOvcEndPtPerEnniCfgLeafSvlanMap,
       "mefServiceOvcEndPtPerEnniCfgIngressBwpGrpIndex": mefServiceOvcEndPtPerEnniCfgIngressBwpGrpIndex,
       "mefServiceOvcEndPtPerEnniCfgEgressBwpGrpIndex": mefServiceOvcEndPtPerEnniCfgEgressBwpGrpIndex,
       "mefServiceOvcEndPtPerEnniCfgRowStatus": mefServiceOvcEndPtPerEnniCfgRowStatus,
       "mefServiceOvcEndPtPerUniCfgTable": mefServiceOvcEndPtPerUniCfgTable,
       "mefServiceOvcEndPtPerUniCfgEntry": mefServiceOvcEndPtPerUniCfgEntry,
       "mefServiceOvcEndPtPerUniCfgIdentifier": mefServiceOvcEndPtPerUniCfgIdentifier,
       "mefServiceOvcEndPtPerUniCfgRole": mefServiceOvcEndPtPerUniCfgRole,
       "mefServiceOvcEndPtPerUniCfgCeVlanMap": mefServiceOvcEndPtPerUniCfgCeVlanMap,
       "mefServiceOvcEndPtPerUniCfgIngressBwpGrpIndex": mefServiceOvcEndPtPerUniCfgIngressBwpGrpIndex,
       "mefServiceOvcEndPtPerUniCfgEgressBwpGrpIndex": mefServiceOvcEndPtPerUniCfgEgressBwpGrpIndex,
       "mefServiceOvcEndPtPerUniCfgRowStatus": mefServiceOvcEndPtPerUniCfgRowStatus,
       "mefServiceOvcEndPtPerVuniCfgTable": mefServiceOvcEndPtPerVuniCfgTable,
       "mefServiceOvcEndPtPerVuniCfgEntry": mefServiceOvcEndPtPerVuniCfgEntry,
       "mefServiceOvcEndPtPerVuniCfgIdentifier": mefServiceOvcEndPtPerVuniCfgIdentifier,
       "mefServiceOvcEndPtPerVuniCfgRole": mefServiceOvcEndPtPerVuniCfgRole,
       "mefServiceOvcEndPtPerVuniCfgCeVlanMap": mefServiceOvcEndPtPerVuniCfgCeVlanMap,
       "mefServiceOvcEndPtPerVuniCfgIngressBwpGrpIndex": mefServiceOvcEndPtPerVuniCfgIngressBwpGrpIndex,
       "mefServiceOvcEndPtPerVuniCfgEgressBwpGrpIndex": mefServiceOvcEndPtPerVuniCfgEgressBwpGrpIndex,
       "mefServiceOvcEndPtPerVuniCfgRowStatus": mefServiceOvcEndPtPerVuniCfgRowStatus,
       "mefServiceEnniOvcMibConformance": mefServiceEnniOvcMibConformance,
       "mefServiceEnniOvcMibCompliances": mefServiceEnniOvcMibCompliances,
       "mefServiceEnniOvcMibCompliance": mefServiceEnniOvcMibCompliance,
       "mefServiceEnniOvcMibGroups": mefServiceEnniOvcMibGroups,
       "mefServiceEnniMandatoryGroup": mefServiceEnniMandatoryGroup,
       "mefServiceVuniOptionalGroup": mefServiceVuniOptionalGroup,
       "mefServiceOvcMandatoryGroup": mefServiceOvcMandatoryGroup,
       "mefServiceOvcPerEndPtPerEnniMandatoryGroup": mefServiceOvcPerEndPtPerEnniMandatoryGroup,
       "mefServiceOvcPerEndPtPerUniMandatoryGroup": mefServiceOvcPerEndPtPerUniMandatoryGroup,
       "mefServiceOvcPerEndPtPerVuniOptionalGroup": mefServiceOvcPerEndPtPerVuniOptionalGroup}
)
