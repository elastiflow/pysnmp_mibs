# SNMP MIB module (ARISTA-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/arista_30065/ARISTA-QOS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:46:36 2025
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

(QueueIndex,) = mibBuilder.importSymbols(
    "ARISTA-QUEUE-MIB",
    "QueueIndex")

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

(PhysicalIndexOrZero,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndexOrZero")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

aristaQosMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13)
)
if mibBuilder.loadTexts:
    aristaQosMib.setRevisions(
        ("2024-11-05 00:00",
         "2024-08-06 00:00",
         "2022-01-11 00:00",
         "2020-05-26 00:00",
         "2018-05-04 00:00",
         "2017-05-24 00:00",
         "2016-11-11 00:00",
         "2016-07-22 00:00",
         "2016-03-21 00:00",
         "2014-08-15 00:00",
         "2014-05-22 00:00",
         "2013-06-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AristaQosMapType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("controlPlane", 1),
          ("dataPlane", 2))
    )



class AristaQosShortId(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )



# MIB Managed Objects in the order of their OIDs

_AristaQosMibObjects_ObjectIdentity = ObjectIdentity
aristaQosMibObjects = _AristaQosMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1)
)
_AristaClassMapTable_Object = MibTable
aristaClassMapTable = _AristaClassMapTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 1)
)
if mibBuilder.loadTexts:
    aristaClassMapTable.setStatus("current")
_AristaClassMapEntry_Object = MibTableRow
aristaClassMapEntry = _AristaClassMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 1, 1)
)
aristaClassMapEntry.setIndexNames(
    (0, "ARISTA-QOS-MIB", "aristaClassMapId"),
    (0, "ARISTA-QOS-MIB", "aristaClassMapType"),
)
if mibBuilder.loadTexts:
    aristaClassMapEntry.setStatus("current")
_AristaClassMapId_Type = AristaQosShortId
_AristaClassMapId_Object = MibTableColumn
aristaClassMapId = _AristaClassMapId_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 1, 1, 1),
    _AristaClassMapId_Type()
)
aristaClassMapId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaClassMapId.setStatus("current")
_AristaClassMapType_Type = AristaQosMapType
_AristaClassMapType_Object = MibTableColumn
aristaClassMapType = _AristaClassMapType_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 1, 1, 2),
    _AristaClassMapType_Type()
)
aristaClassMapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaClassMapType.setStatus("current")


class _AristaClassMapName_Type(DisplayString):
    """Custom type aristaClassMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AristaClassMapName_Type.__name__ = "DisplayString"
_AristaClassMapName_Object = MibTableColumn
aristaClassMapName = _AristaClassMapName_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 1, 1, 3),
    _AristaClassMapName_Type()
)
aristaClassMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaClassMapName.setStatus("current")


class _AristaClassMapMatchCondition_Type(Integer32):
    """Custom type aristaClassMapMatchCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("matchConditionAny", 1),
          ("matchConditionAll", 2))
    )


_AristaClassMapMatchCondition_Type.__name__ = "Integer32"
_AristaClassMapMatchCondition_Object = MibTableColumn
aristaClassMapMatchCondition = _AristaClassMapMatchCondition_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 1, 1, 4),
    _AristaClassMapMatchCondition_Type()
)
aristaClassMapMatchCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaClassMapMatchCondition.setStatus("current")
_AristaClassMapMatchTable_Object = MibTable
aristaClassMapMatchTable = _AristaClassMapMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 2)
)
if mibBuilder.loadTexts:
    aristaClassMapMatchTable.setStatus("current")
_AristaClassMapMatchEntry_Object = MibTableRow
aristaClassMapMatchEntry = _AristaClassMapMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 2, 1)
)
aristaClassMapMatchEntry.setIndexNames(
    (0, "ARISTA-QOS-MIB", "aristaClassMapId"),
    (0, "ARISTA-QOS-MIB", "aristaClassMapType"),
    (0, "ARISTA-QOS-MIB", "aristaClassMapMatchIndex"),
)
if mibBuilder.loadTexts:
    aristaClassMapMatchEntry.setStatus("current")


class _AristaClassMapMatchIndex_Type(Integer32):
    """Custom type aristaClassMapMatchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AristaClassMapMatchIndex_Type.__name__ = "Integer32"
_AristaClassMapMatchIndex_Object = MibTableColumn
aristaClassMapMatchIndex = _AristaClassMapMatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 2, 1, 1),
    _AristaClassMapMatchIndex_Type()
)
aristaClassMapMatchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaClassMapMatchIndex.setStatus("current")


class _AristaClassMapMatchType_Type(Integer32):
    """Custom type aristaClassMapMatchType based on Integer32"""
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
        *(("ipv4AccessGroup", 1),
          ("ipv6AccessGroup", 2),
          ("vlan", 3),
          ("dscpEcn", 4),
          ("mplsTrafficClass", 5),
          ("macAccessGroup", 6))
    )


_AristaClassMapMatchType_Type.__name__ = "Integer32"
_AristaClassMapMatchType_Object = MibTableColumn
aristaClassMapMatchType = _AristaClassMapMatchType_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 2, 1, 2),
    _AristaClassMapMatchType_Type()
)
aristaClassMapMatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaClassMapMatchType.setStatus("current")


class _AristaClassMapMatchName_Type(DisplayString):
    """Custom type aristaClassMapMatchName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AristaClassMapMatchName_Type.__name__ = "DisplayString"
_AristaClassMapMatchName_Object = MibTableColumn
aristaClassMapMatchName = _AristaClassMapMatchName_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 2, 1, 3),
    _AristaClassMapMatchName_Type()
)
aristaClassMapMatchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaClassMapMatchName.setStatus("current")
_AristaPolicyMapTable_Object = MibTable
aristaPolicyMapTable = _AristaPolicyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 3)
)
if mibBuilder.loadTexts:
    aristaPolicyMapTable.setStatus("current")
_AristaPolicyMapEntry_Object = MibTableRow
aristaPolicyMapEntry = _AristaPolicyMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 3, 1)
)
aristaPolicyMapEntry.setIndexNames(
    (0, "ARISTA-QOS-MIB", "aristaPolicyMapId"),
    (0, "ARISTA-QOS-MIB", "aristaPolicyMapType"),
)
if mibBuilder.loadTexts:
    aristaPolicyMapEntry.setStatus("current")
_AristaPolicyMapId_Type = AristaQosShortId
_AristaPolicyMapId_Object = MibTableColumn
aristaPolicyMapId = _AristaPolicyMapId_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 3, 1, 1),
    _AristaPolicyMapId_Type()
)
aristaPolicyMapId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaPolicyMapId.setStatus("current")
_AristaPolicyMapType_Type = AristaQosMapType
_AristaPolicyMapType_Object = MibTableColumn
aristaPolicyMapType = _AristaPolicyMapType_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 3, 1, 2),
    _AristaPolicyMapType_Type()
)
aristaPolicyMapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaPolicyMapType.setStatus("current")


class _AristaPolicyMapName_Type(DisplayString):
    """Custom type aristaPolicyMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AristaPolicyMapName_Type.__name__ = "DisplayString"
_AristaPolicyMapName_Object = MibTableColumn
aristaPolicyMapName = _AristaPolicyMapName_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 3, 1, 3),
    _AristaPolicyMapName_Type()
)
aristaPolicyMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaPolicyMapName.setStatus("current")
_AristaPolicyMapClassTable_Object = MibTable
aristaPolicyMapClassTable = _AristaPolicyMapClassTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 4)
)
if mibBuilder.loadTexts:
    aristaPolicyMapClassTable.setStatus("current")
_AristaPolicyMapClassEntry_Object = MibTableRow
aristaPolicyMapClassEntry = _AristaPolicyMapClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 4, 1)
)
aristaPolicyMapClassEntry.setIndexNames(
    (0, "ARISTA-QOS-MIB", "aristaPolicyMapId"),
    (0, "ARISTA-QOS-MIB", "aristaPolicyMapType"),
    (0, "ARISTA-QOS-MIB", "aristaPolicyMapClassIndex"),
)
if mibBuilder.loadTexts:
    aristaPolicyMapClassEntry.setStatus("current")


class _AristaPolicyMapClassIndex_Type(Integer32):
    """Custom type aristaPolicyMapClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AristaPolicyMapClassIndex_Type.__name__ = "Integer32"
_AristaPolicyMapClassIndex_Object = MibTableColumn
aristaPolicyMapClassIndex = _AristaPolicyMapClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 4, 1, 1),
    _AristaPolicyMapClassIndex_Type()
)
aristaPolicyMapClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaPolicyMapClassIndex.setStatus("current")
_AristaPolicyMapClassId_Type = AristaQosShortId
_AristaPolicyMapClassId_Object = MibTableColumn
aristaPolicyMapClassId = _AristaPolicyMapClassId_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 4, 1, 2),
    _AristaPolicyMapClassId_Type()
)
aristaPolicyMapClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaPolicyMapClassId.setStatus("current")
_AristaPolicyMapActionTable_Object = MibTable
aristaPolicyMapActionTable = _AristaPolicyMapActionTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 5)
)
if mibBuilder.loadTexts:
    aristaPolicyMapActionTable.setStatus("current")
_AristaPolicyMapActionEntry_Object = MibTableRow
aristaPolicyMapActionEntry = _AristaPolicyMapActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 5, 1)
)
aristaPolicyMapActionEntry.setIndexNames(
    (0, "ARISTA-QOS-MIB", "aristaPolicyMapId"),
    (0, "ARISTA-QOS-MIB", "aristaPolicyMapType"),
    (0, "ARISTA-QOS-MIB", "aristaClassMapId"),
    (0, "ARISTA-QOS-MIB", "aristaPolicyMapActionType"),
)
if mibBuilder.loadTexts:
    aristaPolicyMapActionEntry.setStatus("current")


class _AristaPolicyMapActionType_Type(Integer32):
    """Custom type aristaPolicyMapActionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("actionSetShape", 1),
          ("actionSetBandwidth", 2),
          ("actionSetCos", 3),
          ("actionSetDscp", 4),
          ("actionSetTc", 5),
          ("actionSetDrop", 6),
          ("actionSetDropPrecedence", 7))
    )


_AristaPolicyMapActionType_Type.__name__ = "Integer32"
_AristaPolicyMapActionType_Object = MibTableColumn
aristaPolicyMapActionType = _AristaPolicyMapActionType_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 5, 1, 1),
    _AristaPolicyMapActionType_Type()
)
aristaPolicyMapActionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaPolicyMapActionType.setStatus("current")


class _AristaPolicyMapActionRateUnit_Type(Integer32):
    """Custom type aristaPolicyMapActionRateUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rateUnitNone", 0),
          ("rateUnitPps", 1),
          ("rateUnitKbps", 2))
    )


_AristaPolicyMapActionRateUnit_Type.__name__ = "Integer32"
_AristaPolicyMapActionRateUnit_Object = MibTableColumn
aristaPolicyMapActionRateUnit = _AristaPolicyMapActionRateUnit_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 5, 1, 2),
    _AristaPolicyMapActionRateUnit_Type()
)
aristaPolicyMapActionRateUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaPolicyMapActionRateUnit.setStatus("current")
_AristaPolicyMapActionValue_Type = Integer32
_AristaPolicyMapActionValue_Object = MibTableColumn
aristaPolicyMapActionValue = _AristaPolicyMapActionValue_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 5, 1, 3),
    _AristaPolicyMapActionValue_Type()
)
aristaPolicyMapActionValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaPolicyMapActionValue.setStatus("current")
_AristaServicePolicyTable_Object = MibTable
aristaServicePolicyTable = _AristaServicePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 6)
)
if mibBuilder.loadTexts:
    aristaServicePolicyTable.setStatus("current")
_AristaServicePolicyEntry_Object = MibTableRow
aristaServicePolicyEntry = _AristaServicePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 6, 1)
)
aristaServicePolicyEntry.setIndexNames(
    (0, "ARISTA-QOS-MIB", "aristaServicePolicyIfIndex"),
    (0, "ARISTA-QOS-MIB", "aristaServicePolicyDirection"),
)
if mibBuilder.loadTexts:
    aristaServicePolicyEntry.setStatus("current")
_AristaServicePolicyIfIndex_Type = InterfaceIndex
_AristaServicePolicyIfIndex_Object = MibTableColumn
aristaServicePolicyIfIndex = _AristaServicePolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 6, 1, 1),
    _AristaServicePolicyIfIndex_Type()
)
aristaServicePolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaServicePolicyIfIndex.setStatus("current")


class _AristaServicePolicyDirection_Type(Integer32):
    """Custom type aristaServicePolicyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_AristaServicePolicyDirection_Type.__name__ = "Integer32"
_AristaServicePolicyDirection_Object = MibTableColumn
aristaServicePolicyDirection = _AristaServicePolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 6, 1, 2),
    _AristaServicePolicyDirection_Type()
)
aristaServicePolicyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaServicePolicyDirection.setStatus("current")
_AristaServicePolicyMapId_Type = AristaQosShortId
_AristaServicePolicyMapId_Object = MibTableColumn
aristaServicePolicyMapId = _AristaServicePolicyMapId_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 6, 1, 3),
    _AristaServicePolicyMapId_Type()
)
aristaServicePolicyMapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaServicePolicyMapId.setStatus("current")
_AristaServicePolicyMapType_Type = AristaQosMapType
_AristaServicePolicyMapType_Object = MibTableColumn
aristaServicePolicyMapType = _AristaServicePolicyMapType_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 6, 1, 4),
    _AristaServicePolicyMapType_Type()
)
aristaServicePolicyMapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaServicePolicyMapType.setStatus("current")
_AristaQosStatsTable_Object = MibTable
aristaQosStatsTable = _AristaQosStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 7)
)
if mibBuilder.loadTexts:
    aristaQosStatsTable.setStatus("current")
_AristaQosStatsEntry_Object = MibTableRow
aristaQosStatsEntry = _AristaQosStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 7, 1)
)
aristaQosStatsEntry.setIndexNames(
    (0, "ARISTA-QOS-MIB", "aristaPolicyMapId"),
    (0, "ARISTA-QOS-MIB", "aristaPolicyMapType"),
    (0, "ARISTA-QOS-MIB", "aristaClassMapId"),
    (0, "ARISTA-QOS-MIB", "aristaServicePolicyDirection"),
)
if mibBuilder.loadTexts:
    aristaQosStatsEntry.setStatus("current")
_AristaQosPktsDropped_Type = Counter64
_AristaQosPktsDropped_Object = MibTableColumn
aristaQosPktsDropped = _AristaQosPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 7, 1, 1),
    _AristaQosPktsDropped_Type()
)
aristaQosPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaQosPktsDropped.setStatus("current")
_AristaQosPktsSent_Type = Counter64
_AristaQosPktsSent_Object = MibTableColumn
aristaQosPktsSent = _AristaQosPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 7, 1, 2),
    _AristaQosPktsSent_Type()
)
aristaQosPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaQosPktsSent.setStatus("current")
_AristaQosPktsMatched_Type = Counter64
_AristaQosPktsMatched_Object = MibTableColumn
aristaQosPktsMatched = _AristaQosPktsMatched_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 7, 1, 3),
    _AristaQosPktsMatched_Type()
)
aristaQosPktsMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaQosPktsMatched.setStatus("current")
_AristaQosBytesDropped_Type = Counter64
_AristaQosBytesDropped_Object = MibTableColumn
aristaQosBytesDropped = _AristaQosBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 7, 1, 4),
    _AristaQosBytesDropped_Type()
)
aristaQosBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaQosBytesDropped.setStatus("current")
_AristaQosBytesSent_Type = Counter64
_AristaQosBytesSent_Object = MibTableColumn
aristaQosBytesSent = _AristaQosBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 7, 1, 5),
    _AristaQosBytesSent_Type()
)
aristaQosBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaQosBytesSent.setStatus("current")
_AristaQosBytesMatched_Type = Counter64
_AristaQosBytesMatched_Object = MibTableColumn
aristaQosBytesMatched = _AristaQosBytesMatched_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 7, 1, 6),
    _AristaQosBytesMatched_Type()
)
aristaQosBytesMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaQosBytesMatched.setStatus("current")
_AristaEcnCounterTable_Object = MibTable
aristaEcnCounterTable = _AristaEcnCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 8)
)
if mibBuilder.loadTexts:
    aristaEcnCounterTable.setStatus("current")
_AristaEcnCounterEntry_Object = MibTableRow
aristaEcnCounterEntry = _AristaEcnCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 8, 1)
)
aristaEcnCounterEntry.setIndexNames(
    (0, "ARISTA-QOS-MIB", "aristaEcnCounterDescriptor"),
)
if mibBuilder.loadTexts:
    aristaEcnCounterEntry.setStatus("current")


class _AristaEcnCounterDescriptor_Type(DisplayString):
    """Custom type aristaEcnCounterDescriptor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AristaEcnCounterDescriptor_Type.__name__ = "DisplayString"
_AristaEcnCounterDescriptor_Object = MibTableColumn
aristaEcnCounterDescriptor = _AristaEcnCounterDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 8, 1, 1),
    _AristaEcnCounterDescriptor_Type()
)
aristaEcnCounterDescriptor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaEcnCounterDescriptor.setStatus("current")
_AristaEcnCounterValue_Type = Counter64
_AristaEcnCounterValue_Object = MibTableColumn
aristaEcnCounterValue = _AristaEcnCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 8, 1, 2),
    _AristaEcnCounterValue_Type()
)
aristaEcnCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaEcnCounterValue.setStatus("current")
_AristaEcnCounterEntity_Type = PhysicalIndexOrZero
_AristaEcnCounterEntity_Object = MibTableColumn
aristaEcnCounterEntity = _AristaEcnCounterEntity_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 8, 1, 3),
    _AristaEcnCounterEntity_Type()
)
aristaEcnCounterEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaEcnCounterEntity.setStatus("current")
_AristaEcnQueueCounterTable_Object = MibTable
aristaEcnQueueCounterTable = _AristaEcnQueueCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 9)
)
if mibBuilder.loadTexts:
    aristaEcnQueueCounterTable.setStatus("current")
_AristaEcnQueueCounterEntry_Object = MibTableRow
aristaEcnQueueCounterEntry = _AristaEcnQueueCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 9, 1)
)
aristaEcnQueueCounterEntry.setIndexNames(
    (0, "ARISTA-QOS-MIB", "aristaEcnIfIndex"),
    (0, "ARISTA-QOS-MIB", "aristaEcnEgressQueueIndex"),
)
if mibBuilder.loadTexts:
    aristaEcnQueueCounterEntry.setStatus("current")
_AristaEcnIfIndex_Type = InterfaceIndex
_AristaEcnIfIndex_Object = MibTableColumn
aristaEcnIfIndex = _AristaEcnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 9, 1, 1),
    _AristaEcnIfIndex_Type()
)
aristaEcnIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaEcnIfIndex.setStatus("current")
_AristaEcnEgressQueueIndex_Type = QueueIndex
_AristaEcnEgressQueueIndex_Object = MibTableColumn
aristaEcnEgressQueueIndex = _AristaEcnEgressQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 9, 1, 2),
    _AristaEcnEgressQueueIndex_Type()
)
aristaEcnEgressQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaEcnEgressQueueIndex.setStatus("current")
_AristaEcnQueueCounterEnabled_Type = TruthValue
_AristaEcnQueueCounterEnabled_Object = MibTableColumn
aristaEcnQueueCounterEnabled = _AristaEcnQueueCounterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 9, 1, 3),
    _AristaEcnQueueCounterEnabled_Type()
)
aristaEcnQueueCounterEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaEcnQueueCounterEnabled.setStatus("current")
_AristaEcnQueuePktsMarked_Type = Counter64
_AristaEcnQueuePktsMarked_Object = MibTableColumn
aristaEcnQueuePktsMarked = _AristaEcnQueuePktsMarked_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 9, 1, 4),
    _AristaEcnQueuePktsMarked_Type()
)
aristaEcnQueuePktsMarked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaEcnQueuePktsMarked.setStatus("current")
_AristaEcnQueuePktsLocallyMarked_Type = Counter64
_AristaEcnQueuePktsLocallyMarked_Object = MibTableColumn
aristaEcnQueuePktsLocallyMarked = _AristaEcnQueuePktsLocallyMarked_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 9, 1, 5),
    _AristaEcnQueuePktsLocallyMarked_Type()
)
aristaEcnQueuePktsLocallyMarked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaEcnQueuePktsLocallyMarked.setStatus("current")
_AristaQosPolicerStatsTable_Object = MibTable
aristaQosPolicerStatsTable = _AristaQosPolicerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 10)
)
if mibBuilder.loadTexts:
    aristaQosPolicerStatsTable.setStatus("current")
_AristaQosPolicerStatsEntry_Object = MibTableRow
aristaQosPolicerStatsEntry = _AristaQosPolicerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 10, 1)
)
aristaQosPolicerStatsEntry.setIndexNames(
    (0, "ARISTA-QOS-MIB", "aristaPolicyMapId"),
    (0, "ARISTA-QOS-MIB", "aristaPolicyMapType"),
    (0, "ARISTA-QOS-MIB", "aristaClassMapId"),
    (0, "ARISTA-QOS-MIB", "aristaServicePolicyDirection"),
    (0, "ARISTA-QOS-MIB", "aristaServicePolicyIfIndex"),
)
if mibBuilder.loadTexts:
    aristaQosPolicerStatsEntry.setStatus("current")
_AristaQosPolicerPktsDropped_Type = Counter64
_AristaQosPolicerPktsDropped_Object = MibTableColumn
aristaQosPolicerPktsDropped = _AristaQosPolicerPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 10, 1, 1),
    _AristaQosPolicerPktsDropped_Type()
)
aristaQosPolicerPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaQosPolicerPktsDropped.setStatus("current")
_AristaQosPolicerPktsSent_Type = Counter64
_AristaQosPolicerPktsSent_Object = MibTableColumn
aristaQosPolicerPktsSent = _AristaQosPolicerPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 10, 1, 2),
    _AristaQosPolicerPktsSent_Type()
)
aristaQosPolicerPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaQosPolicerPktsSent.setStatus("current")
_AristaQosPerIntfStatsTable_Object = MibTable
aristaQosPerIntfStatsTable = _AristaQosPerIntfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 11)
)
if mibBuilder.loadTexts:
    aristaQosPerIntfStatsTable.setStatus("current")
_AristaQosPerIntfStatsEntry_Object = MibTableRow
aristaQosPerIntfStatsEntry = _AristaQosPerIntfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 11, 1)
)
aristaQosPerIntfStatsEntry.setIndexNames(
    (0, "ARISTA-QOS-MIB", "aristaPolicyMapId"),
    (0, "ARISTA-QOS-MIB", "aristaPolicyMapType"),
    (0, "ARISTA-QOS-MIB", "aristaClassMapId"),
    (0, "ARISTA-QOS-MIB", "aristaServicePolicyDirection"),
    (0, "ARISTA-QOS-MIB", "aristaServicePolicyIfIndex"),
)
if mibBuilder.loadTexts:
    aristaQosPerIntfStatsEntry.setStatus("current")
_AristaQosPerIntfPktsDropped_Type = Counter64
_AristaQosPerIntfPktsDropped_Object = MibTableColumn
aristaQosPerIntfPktsDropped = _AristaQosPerIntfPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 11, 1, 1),
    _AristaQosPerIntfPktsDropped_Type()
)
aristaQosPerIntfPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaQosPerIntfPktsDropped.setStatus("current")
_AristaQosPerIntfPktsSent_Type = Counter64
_AristaQosPerIntfPktsSent_Object = MibTableColumn
aristaQosPerIntfPktsSent = _AristaQosPerIntfPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 11, 1, 2),
    _AristaQosPerIntfPktsSent_Type()
)
aristaQosPerIntfPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaQosPerIntfPktsSent.setStatus("current")
_AristaQosPerIntfPktsMatched_Type = Counter64
_AristaQosPerIntfPktsMatched_Object = MibTableColumn
aristaQosPerIntfPktsMatched = _AristaQosPerIntfPktsMatched_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 11, 1, 3),
    _AristaQosPerIntfPktsMatched_Type()
)
aristaQosPerIntfPktsMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaQosPerIntfPktsMatched.setStatus("current")
_AristaQosPerIntfBytesDropped_Type = Counter64
_AristaQosPerIntfBytesDropped_Object = MibTableColumn
aristaQosPerIntfBytesDropped = _AristaQosPerIntfBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 11, 1, 4),
    _AristaQosPerIntfBytesDropped_Type()
)
aristaQosPerIntfBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaQosPerIntfBytesDropped.setStatus("current")
_AristaQosPerIntfBytesSent_Type = Counter64
_AristaQosPerIntfBytesSent_Object = MibTableColumn
aristaQosPerIntfBytesSent = _AristaQosPerIntfBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 11, 1, 5),
    _AristaQosPerIntfBytesSent_Type()
)
aristaQosPerIntfBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaQosPerIntfBytesSent.setStatus("current")
_AristaQosPerIntfBytesMatched_Type = Counter64
_AristaQosPerIntfBytesMatched_Object = MibTableColumn
aristaQosPerIntfBytesMatched = _AristaQosPerIntfBytesMatched_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 11, 1, 6),
    _AristaQosPerIntfBytesMatched_Type()
)
aristaQosPerIntfBytesMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaQosPerIntfBytesMatched.setStatus("current")
_AristaQosMibConformance_ObjectIdentity = ObjectIdentity
aristaQosMibConformance = _AristaQosMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 2)
)
_AristaQosMibCompliances_ObjectIdentity = ObjectIdentity
aristaQosMibCompliances = _AristaQosMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 2, 1)
)
_AristaQosMibGroups_ObjectIdentity = ObjectIdentity
aristaQosMibGroups = _AristaQosMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 2, 2)
)

# Managed Objects groups

aristaClassMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 2, 2, 1)
)
aristaClassMapGroup.setObjects(
      *(("ARISTA-QOS-MIB", "aristaClassMapName"),
        ("ARISTA-QOS-MIB", "aristaClassMapMatchCondition"),
        ("ARISTA-QOS-MIB", "aristaClassMapMatchType"),
        ("ARISTA-QOS-MIB", "aristaClassMapMatchName"),
        ("ARISTA-QOS-MIB", "aristaPolicyMapClassId"),
        ("ARISTA-QOS-MIB", "aristaQosPktsDropped"),
        ("ARISTA-QOS-MIB", "aristaQosPktsMatched"),
        ("ARISTA-QOS-MIB", "aristaQosPktsSent"),
        ("ARISTA-QOS-MIB", "aristaQosPolicerPktsDropped"),
        ("ARISTA-QOS-MIB", "aristaQosPolicerPktsSent"),
        ("ARISTA-QOS-MIB", "aristaQosBytesDropped"),
        ("ARISTA-QOS-MIB", "aristaQosBytesMatched"),
        ("ARISTA-QOS-MIB", "aristaQosBytesSent"),
        ("ARISTA-QOS-MIB", "aristaQosPerIntfPktsDropped"),
        ("ARISTA-QOS-MIB", "aristaQosPerIntfPktsSent"),
        ("ARISTA-QOS-MIB", "aristaQosPerIntfPktsMatched"),
        ("ARISTA-QOS-MIB", "aristaQosPerIntfBytesDropped"),
        ("ARISTA-QOS-MIB", "aristaQosPerIntfBytesSent"),
        ("ARISTA-QOS-MIB", "aristaQosPerIntfBytesMatched"))
)
if mibBuilder.loadTexts:
    aristaClassMapGroup.setStatus("current")

aristaPolicyMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 2, 2, 2)
)
aristaPolicyMapGroup.setObjects(
    ("ARISTA-QOS-MIB", "aristaPolicyMapName")
)
if mibBuilder.loadTexts:
    aristaPolicyMapGroup.setStatus("current")

aristaPolicyMapActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 2, 2, 3)
)
aristaPolicyMapActionGroup.setObjects(
      *(("ARISTA-QOS-MIB", "aristaPolicyMapActionRateUnit"),
        ("ARISTA-QOS-MIB", "aristaPolicyMapActionValue"))
)
if mibBuilder.loadTexts:
    aristaPolicyMapActionGroup.setStatus("current")

aristaServicePolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 2, 2, 4)
)
aristaServicePolicyGroup.setObjects(
      *(("ARISTA-QOS-MIB", "aristaServicePolicyMapId"),
        ("ARISTA-QOS-MIB", "aristaServicePolicyMapType"))
)
if mibBuilder.loadTexts:
    aristaServicePolicyGroup.setStatus("current")

aristaEcnCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 2, 2, 5)
)
aristaEcnCounterGroup.setObjects(
      *(("ARISTA-QOS-MIB", "aristaEcnCounterValue"),
        ("ARISTA-QOS-MIB", "aristaEcnCounterEntity"))
)
if mibBuilder.loadTexts:
    aristaEcnCounterGroup.setStatus("current")

aristaEcnQueueCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 2, 2, 6)
)
aristaEcnQueueCounterGroup.setObjects(
      *(("ARISTA-QOS-MIB", "aristaEcnQueueCounterEnabled"),
        ("ARISTA-QOS-MIB", "aristaEcnQueuePktsMarked"),
        ("ARISTA-QOS-MIB", "aristaEcnQueuePktsLocallyMarked"))
)
if mibBuilder.loadTexts:
    aristaEcnQueueCounterGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aristaQosMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 13, 2, 1, 1)
)
aristaQosMibCompliance.setObjects(
      *(("ARISTA-QOS-MIB", "aristaClassMapGroup"),
        ("ARISTA-QOS-MIB", "aristaPolicyMapGroup"),
        ("ARISTA-QOS-MIB", "aristaPolicyMapActionGroup"),
        ("ARISTA-QOS-MIB", "aristaServicePolicyGroup"),
        ("ARISTA-QOS-MIB", "aristaEcnCounterGroup"),
        ("ARISTA-QOS-MIB", "aristaEcnQueueCounterGroup"))
)
if mibBuilder.loadTexts:
    aristaQosMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-QOS-MIB",
    **{"AristaQosMapType": AristaQosMapType,
       "AristaQosShortId": AristaQosShortId,
       "aristaQosMib": aristaQosMib,
       "aristaQosMibObjects": aristaQosMibObjects,
       "aristaClassMapTable": aristaClassMapTable,
       "aristaClassMapEntry": aristaClassMapEntry,
       "aristaClassMapId": aristaClassMapId,
       "aristaClassMapType": aristaClassMapType,
       "aristaClassMapName": aristaClassMapName,
       "aristaClassMapMatchCondition": aristaClassMapMatchCondition,
       "aristaClassMapMatchTable": aristaClassMapMatchTable,
       "aristaClassMapMatchEntry": aristaClassMapMatchEntry,
       "aristaClassMapMatchIndex": aristaClassMapMatchIndex,
       "aristaClassMapMatchType": aristaClassMapMatchType,
       "aristaClassMapMatchName": aristaClassMapMatchName,
       "aristaPolicyMapTable": aristaPolicyMapTable,
       "aristaPolicyMapEntry": aristaPolicyMapEntry,
       "aristaPolicyMapId": aristaPolicyMapId,
       "aristaPolicyMapType": aristaPolicyMapType,
       "aristaPolicyMapName": aristaPolicyMapName,
       "aristaPolicyMapClassTable": aristaPolicyMapClassTable,
       "aristaPolicyMapClassEntry": aristaPolicyMapClassEntry,
       "aristaPolicyMapClassIndex": aristaPolicyMapClassIndex,
       "aristaPolicyMapClassId": aristaPolicyMapClassId,
       "aristaPolicyMapActionTable": aristaPolicyMapActionTable,
       "aristaPolicyMapActionEntry": aristaPolicyMapActionEntry,
       "aristaPolicyMapActionType": aristaPolicyMapActionType,
       "aristaPolicyMapActionRateUnit": aristaPolicyMapActionRateUnit,
       "aristaPolicyMapActionValue": aristaPolicyMapActionValue,
       "aristaServicePolicyTable": aristaServicePolicyTable,
       "aristaServicePolicyEntry": aristaServicePolicyEntry,
       "aristaServicePolicyIfIndex": aristaServicePolicyIfIndex,
       "aristaServicePolicyDirection": aristaServicePolicyDirection,
       "aristaServicePolicyMapId": aristaServicePolicyMapId,
       "aristaServicePolicyMapType": aristaServicePolicyMapType,
       "aristaQosStatsTable": aristaQosStatsTable,
       "aristaQosStatsEntry": aristaQosStatsEntry,
       "aristaQosPktsDropped": aristaQosPktsDropped,
       "aristaQosPktsSent": aristaQosPktsSent,
       "aristaQosPktsMatched": aristaQosPktsMatched,
       "aristaQosBytesDropped": aristaQosBytesDropped,
       "aristaQosBytesSent": aristaQosBytesSent,
       "aristaQosBytesMatched": aristaQosBytesMatched,
       "aristaEcnCounterTable": aristaEcnCounterTable,
       "aristaEcnCounterEntry": aristaEcnCounterEntry,
       "aristaEcnCounterDescriptor": aristaEcnCounterDescriptor,
       "aristaEcnCounterValue": aristaEcnCounterValue,
       "aristaEcnCounterEntity": aristaEcnCounterEntity,
       "aristaEcnQueueCounterTable": aristaEcnQueueCounterTable,
       "aristaEcnQueueCounterEntry": aristaEcnQueueCounterEntry,
       "aristaEcnIfIndex": aristaEcnIfIndex,
       "aristaEcnEgressQueueIndex": aristaEcnEgressQueueIndex,
       "aristaEcnQueueCounterEnabled": aristaEcnQueueCounterEnabled,
       "aristaEcnQueuePktsMarked": aristaEcnQueuePktsMarked,
       "aristaEcnQueuePktsLocallyMarked": aristaEcnQueuePktsLocallyMarked,
       "aristaQosPolicerStatsTable": aristaQosPolicerStatsTable,
       "aristaQosPolicerStatsEntry": aristaQosPolicerStatsEntry,
       "aristaQosPolicerPktsDropped": aristaQosPolicerPktsDropped,
       "aristaQosPolicerPktsSent": aristaQosPolicerPktsSent,
       "aristaQosPerIntfStatsTable": aristaQosPerIntfStatsTable,
       "aristaQosPerIntfStatsEntry": aristaQosPerIntfStatsEntry,
       "aristaQosPerIntfPktsDropped": aristaQosPerIntfPktsDropped,
       "aristaQosPerIntfPktsSent": aristaQosPerIntfPktsSent,
       "aristaQosPerIntfPktsMatched": aristaQosPerIntfPktsMatched,
       "aristaQosPerIntfBytesDropped": aristaQosPerIntfBytesDropped,
       "aristaQosPerIntfBytesSent": aristaQosPerIntfBytesSent,
       "aristaQosPerIntfBytesMatched": aristaQosPerIntfBytesMatched,
       "aristaQosMibConformance": aristaQosMibConformance,
       "aristaQosMibCompliances": aristaQosMibCompliances,
       "aristaQosMibCompliance": aristaQosMibCompliance,
       "aristaQosMibGroups": aristaQosMibGroups,
       "aristaClassMapGroup": aristaClassMapGroup,
       "aristaPolicyMapGroup": aristaPolicyMapGroup,
       "aristaPolicyMapActionGroup": aristaPolicyMapActionGroup,
       "aristaServicePolicyGroup": aristaServicePolicyGroup,
       "aristaEcnCounterGroup": aristaEcnCounterGroup,
       "aristaEcnQueueCounterGroup": aristaEcnQueueCounterGroup}
)
