# SNMP MIB module (BELAIR-QOS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_15768/BELAIR-QOS.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:08:43 2025
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

(belairApplications,
 belairModules) = mibBuilder.importSymbols(
    "BELAIR-SMI",
    "belairApplications",
    "belairModules")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

belairQoSModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 1, 6)
)
if mibBuilder.loadTexts:
    belairQoSModule.setRevisions(
        ("2007-06-01 16:00",
         "2006-03-07 19:32",
         "2006-01-17 17:12",
         "2005-11-17 15:11",
         "2005-11-11 16:35",
         "2005-07-20 11:22")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ConfigStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("default", 2))
    )



class QueueId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )



class VlanId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2815),
    )



# MIB Managed Objects in the order of their OIDs

_BelairQosObjects_ObjectIdentity = ObjectIdentity
belairQosObjects = _BelairQosObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1)
)
if mibBuilder.loadTexts:
    belairQosObjects.setStatus("current")
_BelairQosGlobalControl_ObjectIdentity = ObjectIdentity
belairQosGlobalControl = _BelairQosGlobalControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 1)
)
if mibBuilder.loadTexts:
    belairQosGlobalControl.setStatus("current")


class _BelairQosConfiguration_Type(ConfigStatus):
    """Custom type belairQosConfiguration based on ConfigStatus"""
    subtypeSpec = ConfigStatus.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_BelairQosConfiguration_Type.__name__ = "ConfigStatus"
_BelairQosConfiguration_Object = MibScalar
belairQosConfiguration = _BelairQosConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 1, 1),
    _BelairQosConfiguration_Type()
)
belairQosConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairQosConfiguration.setStatus("current")


class _BelairQosSVPClassification_Type(Integer32):
    """Custom type belairQosSVPClassification based on Integer32"""
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


_BelairQosSVPClassification_Type.__name__ = "Integer32"
_BelairQosSVPClassification_Object = MibScalar
belairQosSVPClassification = _BelairQosSVPClassification_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 1, 2),
    _BelairQosSVPClassification_Type()
)
belairQosSVPClassification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairQosSVPClassification.setStatus("current")
_BelairQosUPtoQueueMapTable_Object = MibTable
belairQosUPtoQueueMapTable = _BelairQosUPtoQueueMapTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 1, 3)
)
if mibBuilder.loadTexts:
    belairQosUPtoQueueMapTable.setStatus("current")
_BelairQosUPtoQueueMapEntry_Object = MibTableRow
belairQosUPtoQueueMapEntry = _BelairQosUPtoQueueMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 1, 3, 1)
)
belairQosUPtoQueueMapEntry.setIndexNames(
    (0, "BELAIR-QOS", "belairQosUPValue"),
)
if mibBuilder.loadTexts:
    belairQosUPtoQueueMapEntry.setStatus("current")


class _BelairQosUPValue_Type(Integer32):
    """Custom type belairQosUPValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BelairQosUPValue_Type.__name__ = "Integer32"
_BelairQosUPValue_Object = MibTableColumn
belairQosUPValue = _BelairQosUPValue_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 1, 3, 1, 1),
    _BelairQosUPValue_Type()
)
belairQosUPValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairQosUPValue.setStatus("current")
_BelairQosUPtoQueue_Type = QueueId
_BelairQosUPtoQueue_Object = MibTableColumn
belairQosUPtoQueue = _BelairQosUPtoQueue_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 1, 3, 1, 2),
    _BelairQosUPtoQueue_Type()
)
belairQosUPtoQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairQosUPtoQueue.setStatus("current")
_BelairQosTOStoUPMapTable_Object = MibTable
belairQosTOStoUPMapTable = _BelairQosTOStoUPMapTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 1, 4)
)
if mibBuilder.loadTexts:
    belairQosTOStoUPMapTable.setStatus("current")
_BelairQosTOStoUPMapEntry_Object = MibTableRow
belairQosTOStoUPMapEntry = _BelairQosTOStoUPMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 1, 4, 1)
)
belairQosTOStoUPMapEntry.setIndexNames(
    (0, "BELAIR-QOS", "belairQosTOSValue"),
)
if mibBuilder.loadTexts:
    belairQosTOStoUPMapEntry.setStatus("current")


class _BelairQosTOSValue_Type(Integer32):
    """Custom type belairQosTOSValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_BelairQosTOSValue_Type.__name__ = "Integer32"
_BelairQosTOSValue_Object = MibTableColumn
belairQosTOSValue = _BelairQosTOSValue_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 1, 4, 1, 1),
    _BelairQosTOSValue_Type()
)
belairQosTOSValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairQosTOSValue.setStatus("current")


class _BelairQosTOStoUPValue_Type(Integer32):
    """Custom type belairQosTOStoUPValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BelairQosTOStoUPValue_Type.__name__ = "Integer32"
_BelairQosTOStoUPValue_Object = MibTableColumn
belairQosTOStoUPValue = _BelairQosTOStoUPValue_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 1, 4, 1, 2),
    _BelairQosTOStoUPValue_Type()
)
belairQosTOStoUPValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairQosTOStoUPValue.setStatus("current")
_BelairQosVlan_ObjectIdentity = ObjectIdentity
belairQosVlan = _BelairQosVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2)
)
if mibBuilder.loadTexts:
    belairQosVlan.setStatus("current")
_BelairQosVlanListTable_Object = MibTable
belairQosVlanListTable = _BelairQosVlanListTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    belairQosVlanListTable.setStatus("current")
_BelairQosVlanListEntry_Object = MibTableRow
belairQosVlanListEntry = _BelairQosVlanListEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 1, 1)
)
belairQosVlanListEntry.setIndexNames(
    (0, "BELAIR-QOS", "belairQosVlanInterfaceIndex"),
)
if mibBuilder.loadTexts:
    belairQosVlanListEntry.setStatus("current")
_BelairQosVlanInterfaceIndex_Type = VlanId
_BelairQosVlanInterfaceIndex_Object = MibTableColumn
belairQosVlanInterfaceIndex = _BelairQosVlanInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 1, 1, 1),
    _BelairQosVlanInterfaceIndex_Type()
)
belairQosVlanInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairQosVlanInterfaceIndex.setStatus("current")


class _BelairQosVlanStatus_Type(ConfigStatus):
    """Custom type belairQosVlanStatus based on ConfigStatus"""
    subtypeSpec = ConfigStatus.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_BelairQosVlanStatus_Type.__name__ = "ConfigStatus"
_BelairQosVlanStatus_Object = MibTableColumn
belairQosVlanStatus = _BelairQosVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 1, 1, 2),
    _BelairQosVlanStatus_Type()
)
belairQosVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairQosVlanStatus.setStatus("current")


class _BelairQosVlanUserPriority_Type(Integer32):
    """Custom type belairQosVlanUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BelairQosVlanUserPriority_Type.__name__ = "Integer32"
_BelairQosVlanUserPriority_Object = MibTableColumn
belairQosVlanUserPriority = _BelairQosVlanUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 1, 1, 3),
    _BelairQosVlanUserPriority_Type()
)
belairQosVlanUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairQosVlanUserPriority.setStatus("current")
_BelairQosVlanQueueId_Type = QueueId
_BelairQosVlanQueueId_Object = MibTableColumn
belairQosVlanQueueId = _BelairQosVlanQueueId_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 1, 1, 4),
    _BelairQosVlanQueueId_Type()
)
belairQosVlanQueueId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairQosVlanQueueId.setStatus("current")


class _BelairQosVlanAverageRate_Type(Integer32):
    """Custom type belairQosVlanAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(190, 100000),
    )


_BelairQosVlanAverageRate_Type.__name__ = "Integer32"
_BelairQosVlanAverageRate_Object = MibTableColumn
belairQosVlanAverageRate = _BelairQosVlanAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 1, 1, 5),
    _BelairQosVlanAverageRate_Type()
)
belairQosVlanAverageRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairQosVlanAverageRate.setStatus("current")
if mibBuilder.loadTexts:
    belairQosVlanAverageRate.setUnits("kbps")


class _BelairQosVlanBurstSize_Type(Integer32):
    """Custom type belairQosVlanBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 1048575),
    )


_BelairQosVlanBurstSize_Type.__name__ = "Integer32"
_BelairQosVlanBurstSize_Object = MibTableColumn
belairQosVlanBurstSize = _BelairQosVlanBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 1, 1, 6),
    _BelairQosVlanBurstSize_Type()
)
belairQosVlanBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairQosVlanBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    belairQosVlanBurstSize.setUnits("bytes")
_BelairQosVlanToStoUPListTable_Object = MibTable
belairQosVlanToStoUPListTable = _BelairQosVlanToStoUPListTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    belairQosVlanToStoUPListTable.setStatus("current")
_BelairQosVlanToStoUPListEntry_Object = MibTableRow
belairQosVlanToStoUPListEntry = _BelairQosVlanToStoUPListEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 2, 1)
)
belairQosVlanToStoUPListEntry.setIndexNames(
    (0, "BELAIR-QOS", "belairQosToSVlanId"),
    (0, "BELAIR-QOS", "belairQosVlanTOSValue"),
)
if mibBuilder.loadTexts:
    belairQosVlanToStoUPListEntry.setStatus("current")
_BelairQosToSVlanId_Type = VlanId
_BelairQosToSVlanId_Object = MibTableColumn
belairQosToSVlanId = _BelairQosToSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 2, 1, 1),
    _BelairQosToSVlanId_Type()
)
belairQosToSVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairQosToSVlanId.setStatus("current")


class _BelairQosVlanTOSValue_Type(Integer32):
    """Custom type belairQosVlanTOSValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_BelairQosVlanTOSValue_Type.__name__ = "Integer32"
_BelairQosVlanTOSValue_Object = MibTableColumn
belairQosVlanTOSValue = _BelairQosVlanTOSValue_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 2, 1, 2),
    _BelairQosVlanTOSValue_Type()
)
belairQosVlanTOSValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairQosVlanTOSValue.setStatus("current")


class _BelairQosVlanTOStoUPValue_Type(Integer32):
    """Custom type belairQosVlanTOStoUPValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BelairQosVlanTOStoUPValue_Type.__name__ = "Integer32"
_BelairQosVlanTOStoUPValue_Object = MibTableColumn
belairQosVlanTOStoUPValue = _BelairQosVlanTOStoUPValue_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 2, 1, 3),
    _BelairQosVlanTOStoUPValue_Type()
)
belairQosVlanTOStoUPValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairQosVlanTOStoUPValue.setStatus("current")


class _BelairQosVlanTostoUpAverageRate_Type(Integer32):
    """Custom type belairQosVlanTostoUpAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(190, 100000),
    )


_BelairQosVlanTostoUpAverageRate_Type.__name__ = "Integer32"
_BelairQosVlanTostoUpAverageRate_Object = MibTableColumn
belairQosVlanTostoUpAverageRate = _BelairQosVlanTostoUpAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 2, 1, 4),
    _BelairQosVlanTostoUpAverageRate_Type()
)
belairQosVlanTostoUpAverageRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairQosVlanTostoUpAverageRate.setStatus("current")
if mibBuilder.loadTexts:
    belairQosVlanTostoUpAverageRate.setUnits("kbps")


class _BelairQosVlanTostoUpBurstSize_Type(Integer32):
    """Custom type belairQosVlanTostoUpBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 1048575),
    )


_BelairQosVlanTostoUpBurstSize_Type.__name__ = "Integer32"
_BelairQosVlanTostoUpBurstSize_Object = MibTableColumn
belairQosVlanTostoUpBurstSize = _BelairQosVlanTostoUpBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 2, 1, 5),
    _BelairQosVlanTostoUpBurstSize_Type()
)
belairQosVlanTostoUpBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairQosVlanTostoUpBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    belairQosVlanTostoUpBurstSize.setUnits("bytes")
_BelairVlanCurrentStatsTable_Object = MibTable
belairVlanCurrentStatsTable = _BelairVlanCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 3)
)
if mibBuilder.loadTexts:
    belairVlanCurrentStatsTable.setStatus("current")
_BelairVlanCurrentStatsEntry_Object = MibTableRow
belairVlanCurrentStatsEntry = _BelairVlanCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 3, 1)
)
belairVlanCurrentStatsEntry.setIndexNames(
    (0, "BELAIR-QOS", "belairPerfVlanId"),
)
if mibBuilder.loadTexts:
    belairVlanCurrentStatsEntry.setStatus("current")
_BelairPerfVlanId_Type = VlanId
_BelairPerfVlanId_Object = MibTableColumn
belairPerfVlanId = _BelairPerfVlanId_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 3, 1, 1),
    _BelairPerfVlanId_Type()
)
belairPerfVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairPerfVlanId.setStatus("current")
_BelairPerfCurrVlanPackets_Type = Counter64
_BelairPerfCurrVlanPackets_Object = MibTableColumn
belairPerfCurrVlanPackets = _BelairPerfCurrVlanPackets_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 3, 1, 3),
    _BelairPerfCurrVlanPackets_Type()
)
belairPerfCurrVlanPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairPerfCurrVlanPackets.setStatus("current")
if mibBuilder.loadTexts:
    belairPerfCurrVlanPackets.setUnits("packets")
_BelairPerfCurrVlanOctets_Type = Counter64
_BelairPerfCurrVlanOctets_Object = MibTableColumn
belairPerfCurrVlanOctets = _BelairPerfCurrVlanOctets_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 3, 1, 4),
    _BelairPerfCurrVlanOctets_Type()
)
belairPerfCurrVlanOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairPerfCurrVlanOctets.setStatus("current")
if mibBuilder.loadTexts:
    belairPerfCurrVlanOctets.setUnits("octets")
_BelairVlanIntervalStatsTable_Object = MibTable
belairVlanIntervalStatsTable = _BelairVlanIntervalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 4)
)
if mibBuilder.loadTexts:
    belairVlanIntervalStatsTable.setStatus("current")
_BelairVlanIntervalStatsEntry_Object = MibTableRow
belairVlanIntervalStatsEntry = _BelairVlanIntervalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 4, 1)
)
belairVlanIntervalStatsEntry.setIndexNames(
    (0, "BELAIR-QOS", "belairPerfIntervalNumber"),
    (0, "BELAIR-QOS", "belairPerfIntervalVlanId"),
)
if mibBuilder.loadTexts:
    belairVlanIntervalStatsEntry.setStatus("current")
_BelairPerfIntervalVlanId_Type = VlanId
_BelairPerfIntervalVlanId_Object = MibTableColumn
belairPerfIntervalVlanId = _BelairPerfIntervalVlanId_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 4, 1, 1),
    _BelairPerfIntervalVlanId_Type()
)
belairPerfIntervalVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairPerfIntervalVlanId.setStatus("current")


class _BelairPerfIntervalNumber_Type(Integer32):
    """Custom type belairPerfIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_BelairPerfIntervalNumber_Type.__name__ = "Integer32"
_BelairPerfIntervalNumber_Object = MibTableColumn
belairPerfIntervalNumber = _BelairPerfIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 4, 1, 2),
    _BelairPerfIntervalNumber_Type()
)
belairPerfIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairPerfIntervalNumber.setStatus("current")
_BelairPerfIntervalVlanPackets_Type = Counter64
_BelairPerfIntervalVlanPackets_Object = MibTableColumn
belairPerfIntervalVlanPackets = _BelairPerfIntervalVlanPackets_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 4, 1, 3),
    _BelairPerfIntervalVlanPackets_Type()
)
belairPerfIntervalVlanPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairPerfIntervalVlanPackets.setStatus("current")
if mibBuilder.loadTexts:
    belairPerfIntervalVlanPackets.setUnits("packets")
_BelairPerfIntervalVlanOctets_Type = Counter64
_BelairPerfIntervalVlanOctets_Object = MibTableColumn
belairPerfIntervalVlanOctets = _BelairPerfIntervalVlanOctets_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 2, 4, 1, 4),
    _BelairPerfIntervalVlanOctets_Type()
)
belairPerfIntervalVlanOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairPerfIntervalVlanOctets.setStatus("current")
if mibBuilder.loadTexts:
    belairPerfIntervalVlanOctets.setUnits("octets")
_BelairQosMac_ObjectIdentity = ObjectIdentity
belairQosMac = _BelairQosMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 3)
)
if mibBuilder.loadTexts:
    belairQosMac.setStatus("current")
_BelairQosMacListTable_Object = MibTable
belairQosMacListTable = _BelairQosMacListTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    belairQosMacListTable.setStatus("current")
_BelairQosMacListEntry_Object = MibTableRow
belairQosMacListEntry = _BelairQosMacListEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 3, 1, 1)
)
belairQosMacListEntry.setIndexNames(
    (0, "BELAIR-QOS", "belairQosMacIndex"),
)
if mibBuilder.loadTexts:
    belairQosMacListEntry.setStatus("current")


class _BelairQosMacIndex_Type(Integer32):
    """Custom type belairQosMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BelairQosMacIndex_Type.__name__ = "Integer32"
_BelairQosMacIndex_Object = MibTableColumn
belairQosMacIndex = _BelairQosMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 3, 1, 1, 1),
    _BelairQosMacIndex_Type()
)
belairQosMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairQosMacIndex.setStatus("current")
_BelairQosMacAddr_Type = MacAddress
_BelairQosMacAddr_Object = MibTableColumn
belairQosMacAddr = _BelairQosMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 3, 1, 1, 2),
    _BelairQosMacAddr_Type()
)
belairQosMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairQosMacAddr.setStatus("current")
_BelairQosMacVid_Type = VlanId
_BelairQosMacVid_Object = MibTableColumn
belairQosMacVid = _BelairQosMacVid_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 3, 1, 1, 3),
    _BelairQosMacVid_Type()
)
belairQosMacVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairQosMacVid.setStatus("current")


class _BelairQosMacVlanUserPriority_Type(Integer32):
    """Custom type belairQosMacVlanUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BelairQosMacVlanUserPriority_Type.__name__ = "Integer32"
_BelairQosMacVlanUserPriority_Object = MibTableColumn
belairQosMacVlanUserPriority = _BelairQosMacVlanUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 3, 1, 1, 4),
    _BelairQosMacVlanUserPriority_Type()
)
belairQosMacVlanUserPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairQosMacVlanUserPriority.setStatus("current")


class _BelairQosMacType_Type(Integer32):
    """Custom type belairQosMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BelairQosMacType_Type.__name__ = "Integer32"
_BelairQosMacType_Object = MibTableColumn
belairQosMacType = _BelairQosMacType_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 3, 1, 1, 5),
    _BelairQosMacType_Type()
)
belairQosMacType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairQosMacType.setStatus("current")


class _BelairQosMacAverageRate_Type(Integer32):
    """Custom type belairQosMacAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(190, 100000),
    )


_BelairQosMacAverageRate_Type.__name__ = "Integer32"
_BelairQosMacAverageRate_Object = MibTableColumn
belairQosMacAverageRate = _BelairQosMacAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 3, 1, 1, 6),
    _BelairQosMacAverageRate_Type()
)
belairQosMacAverageRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairQosMacAverageRate.setStatus("current")
if mibBuilder.loadTexts:
    belairQosMacAverageRate.setUnits("kbps")


class _BelairQosMacBurstSize_Type(Integer32):
    """Custom type belairQosMacBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 1048575),
    )


_BelairQosMacBurstSize_Type.__name__ = "Integer32"
_BelairQosMacBurstSize_Object = MibTableColumn
belairQosMacBurstSize = _BelairQosMacBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 3, 1, 1, 7),
    _BelairQosMacBurstSize_Type()
)
belairQosMacBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairQosMacBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    belairQosMacBurstSize.setUnits("bytes")
_BelairQosMacStatus_Type = RowStatus
_BelairQosMacStatus_Object = MibTableColumn
belairQosMacStatus = _BelairQosMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 3, 1, 1, 8),
    _BelairQosMacStatus_Type()
)
belairQosMacStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairQosMacStatus.setStatus("current")
_BelairQosIp_ObjectIdentity = ObjectIdentity
belairQosIp = _BelairQosIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 4)
)
if mibBuilder.loadTexts:
    belairQosIp.setStatus("current")
_BelairQosIpListTable_Object = MibTable
belairQosIpListTable = _BelairQosIpListTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 4, 1)
)
if mibBuilder.loadTexts:
    belairQosIpListTable.setStatus("current")
_BelairQosIpListEntry_Object = MibTableRow
belairQosIpListEntry = _BelairQosIpListEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 4, 1, 1)
)
belairQosIpListEntry.setIndexNames(
    (0, "BELAIR-QOS", "belairQosIpIndex"),
)
if mibBuilder.loadTexts:
    belairQosIpListEntry.setStatus("current")


class _BelairQosIpIndex_Type(Integer32):
    """Custom type belairQosIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2879),
    )


_BelairQosIpIndex_Type.__name__ = "Integer32"
_BelairQosIpIndex_Object = MibTableColumn
belairQosIpIndex = _BelairQosIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 4, 1, 1, 1),
    _BelairQosIpIndex_Type()
)
belairQosIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairQosIpIndex.setStatus("current")
_BelairQosIpAddr_Type = IpAddress
_BelairQosIpAddr_Object = MibTableColumn
belairQosIpAddr = _BelairQosIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 4, 1, 1, 2),
    _BelairQosIpAddr_Type()
)
belairQosIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairQosIpAddr.setStatus("current")
_BelairQosIpVid_Type = VlanId
_BelairQosIpVid_Object = MibTableColumn
belairQosIpVid = _BelairQosIpVid_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 4, 1, 1, 3),
    _BelairQosIpVid_Type()
)
belairQosIpVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairQosIpVid.setStatus("current")


class _BelairQosIpVlanUserPriority_Type(Integer32):
    """Custom type belairQosIpVlanUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BelairQosIpVlanUserPriority_Type.__name__ = "Integer32"
_BelairQosIpVlanUserPriority_Object = MibTableColumn
belairQosIpVlanUserPriority = _BelairQosIpVlanUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 4, 1, 1, 4),
    _BelairQosIpVlanUserPriority_Type()
)
belairQosIpVlanUserPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairQosIpVlanUserPriority.setStatus("current")


class _BelairQosIpType_Type(Integer32):
    """Custom type belairQosIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BelairQosIpType_Type.__name__ = "Integer32"
_BelairQosIpType_Object = MibTableColumn
belairQosIpType = _BelairQosIpType_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 4, 1, 1, 5),
    _BelairQosIpType_Type()
)
belairQosIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairQosIpType.setStatus("current")


class _BelairQosIpAverageRate_Type(Integer32):
    """Custom type belairQosIpAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(190, 100000),
    )


_BelairQosIpAverageRate_Type.__name__ = "Integer32"
_BelairQosIpAverageRate_Object = MibTableColumn
belairQosIpAverageRate = _BelairQosIpAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 4, 1, 1, 6),
    _BelairQosIpAverageRate_Type()
)
belairQosIpAverageRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairQosIpAverageRate.setStatus("current")
if mibBuilder.loadTexts:
    belairQosIpAverageRate.setUnits("kbps")


class _BelairQosIpBurstSize_Type(Integer32):
    """Custom type belairQosIpBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 1048575),
    )


_BelairQosIpBurstSize_Type.__name__ = "Integer32"
_BelairQosIpBurstSize_Object = MibTableColumn
belairQosIpBurstSize = _BelairQosIpBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 4, 1, 1, 7),
    _BelairQosIpBurstSize_Type()
)
belairQosIpBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairQosIpBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    belairQosIpBurstSize.setUnits("bytes")
_BelairQosIpStatus_Type = RowStatus
_BelairQosIpStatus_Object = MibTableColumn
belairQosIpStatus = _BelairQosIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 6, 1, 4, 1, 1, 8),
    _BelairQosIpStatus_Type()
)
belairQosIpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairQosIpStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BELAIR-QOS",
    **{"ConfigStatus": ConfigStatus,
       "QueueId": QueueId,
       "VlanId": VlanId,
       "belairQoSModule": belairQoSModule,
       "belairQosObjects": belairQosObjects,
       "belairQosGlobalControl": belairQosGlobalControl,
       "belairQosConfiguration": belairQosConfiguration,
       "belairQosSVPClassification": belairQosSVPClassification,
       "belairQosUPtoQueueMapTable": belairQosUPtoQueueMapTable,
       "belairQosUPtoQueueMapEntry": belairQosUPtoQueueMapEntry,
       "belairQosUPValue": belairQosUPValue,
       "belairQosUPtoQueue": belairQosUPtoQueue,
       "belairQosTOStoUPMapTable": belairQosTOStoUPMapTable,
       "belairQosTOStoUPMapEntry": belairQosTOStoUPMapEntry,
       "belairQosTOSValue": belairQosTOSValue,
       "belairQosTOStoUPValue": belairQosTOStoUPValue,
       "belairQosVlan": belairQosVlan,
       "belairQosVlanListTable": belairQosVlanListTable,
       "belairQosVlanListEntry": belairQosVlanListEntry,
       "belairQosVlanInterfaceIndex": belairQosVlanInterfaceIndex,
       "belairQosVlanStatus": belairQosVlanStatus,
       "belairQosVlanUserPriority": belairQosVlanUserPriority,
       "belairQosVlanQueueId": belairQosVlanQueueId,
       "belairQosVlanAverageRate": belairQosVlanAverageRate,
       "belairQosVlanBurstSize": belairQosVlanBurstSize,
       "belairQosVlanToStoUPListTable": belairQosVlanToStoUPListTable,
       "belairQosVlanToStoUPListEntry": belairQosVlanToStoUPListEntry,
       "belairQosToSVlanId": belairQosToSVlanId,
       "belairQosVlanTOSValue": belairQosVlanTOSValue,
       "belairQosVlanTOStoUPValue": belairQosVlanTOStoUPValue,
       "belairQosVlanTostoUpAverageRate": belairQosVlanTostoUpAverageRate,
       "belairQosVlanTostoUpBurstSize": belairQosVlanTostoUpBurstSize,
       "belairVlanCurrentStatsTable": belairVlanCurrentStatsTable,
       "belairVlanCurrentStatsEntry": belairVlanCurrentStatsEntry,
       "belairPerfVlanId": belairPerfVlanId,
       "belairPerfCurrVlanPackets": belairPerfCurrVlanPackets,
       "belairPerfCurrVlanOctets": belairPerfCurrVlanOctets,
       "belairVlanIntervalStatsTable": belairVlanIntervalStatsTable,
       "belairVlanIntervalStatsEntry": belairVlanIntervalStatsEntry,
       "belairPerfIntervalVlanId": belairPerfIntervalVlanId,
       "belairPerfIntervalNumber": belairPerfIntervalNumber,
       "belairPerfIntervalVlanPackets": belairPerfIntervalVlanPackets,
       "belairPerfIntervalVlanOctets": belairPerfIntervalVlanOctets,
       "belairQosMac": belairQosMac,
       "belairQosMacListTable": belairQosMacListTable,
       "belairQosMacListEntry": belairQosMacListEntry,
       "belairQosMacIndex": belairQosMacIndex,
       "belairQosMacAddr": belairQosMacAddr,
       "belairQosMacVid": belairQosMacVid,
       "belairQosMacVlanUserPriority": belairQosMacVlanUserPriority,
       "belairQosMacType": belairQosMacType,
       "belairQosMacAverageRate": belairQosMacAverageRate,
       "belairQosMacBurstSize": belairQosMacBurstSize,
       "belairQosMacStatus": belairQosMacStatus,
       "belairQosIp": belairQosIp,
       "belairQosIpListTable": belairQosIpListTable,
       "belairQosIpListEntry": belairQosIpListEntry,
       "belairQosIpIndex": belairQosIpIndex,
       "belairQosIpAddr": belairQosIpAddr,
       "belairQosIpVid": belairQosIpVid,
       "belairQosIpVlanUserPriority": belairQosIpVlanUserPriority,
       "belairQosIpType": belairQosIpType,
       "belairQosIpAverageRate": belairQosIpAverageRate,
       "belairQosIpBurstSize": belairQosIpBurstSize,
       "belairQosIpStatus": belairQosIpStatus}
)
