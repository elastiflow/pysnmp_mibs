# SNMP MIB module (DNOS-BOXSERVICES-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/dell_674/DNOS-BOXSERVICES-PRIVATE-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:25:38 2025
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

(dnOS,) = mibBuilder.importSymbols(
    "DELL-REF-MIB",
    "dnOS")

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

fastPathBoxServices = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43)
)
if mibBuilder.loadTexts:
    fastPathBoxServices.setRevisions(
        ("2011-01-26 00:00",
         "2008-02-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class BoxsTemperatureStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("normal", 1),
          ("warning", 2),
          ("critical", 3),
          ("shutdown", 4),
          ("notpresent", 5),
          ("notoperational", 6))
    )



# MIB Managed Objects in the order of their OIDs

_FastPathBoxServicesTraps_ObjectIdentity = ObjectIdentity
fastPathBoxServicesTraps = _FastPathBoxServicesTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 0)
)
_BoxServicesGroup_ObjectIdentity = ObjectIdentity
boxServicesGroup = _BoxServicesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1)
)


class _BoxServicesNormalTempRangeMin_Type(Integer32):
    """Custom type boxServicesNormalTempRangeMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_BoxServicesNormalTempRangeMin_Type.__name__ = "Integer32"
_BoxServicesNormalTempRangeMin_Object = MibScalar
boxServicesNormalTempRangeMin = _BoxServicesNormalTempRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 1),
    _BoxServicesNormalTempRangeMin_Type()
)
boxServicesNormalTempRangeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boxServicesNormalTempRangeMin.setStatus("current")


class _BoxServicesNormalTempRangeMax_Type(Integer32):
    """Custom type boxServicesNormalTempRangeMax based on Integer32"""
    defaultValue = 45

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_BoxServicesNormalTempRangeMax_Type.__name__ = "Integer32"
_BoxServicesNormalTempRangeMax_Object = MibScalar
boxServicesNormalTempRangeMax = _BoxServicesNormalTempRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 2),
    _BoxServicesNormalTempRangeMax_Type()
)
boxServicesNormalTempRangeMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boxServicesNormalTempRangeMax.setStatus("current")


class _BoxServicesTemperatureTrapEnable_Type(Integer32):
    """Custom type boxServicesTemperatureTrapEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_BoxServicesTemperatureTrapEnable_Type.__name__ = "Integer32"
_BoxServicesTemperatureTrapEnable_Object = MibScalar
boxServicesTemperatureTrapEnable = _BoxServicesTemperatureTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 3),
    _BoxServicesTemperatureTrapEnable_Type()
)
boxServicesTemperatureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boxServicesTemperatureTrapEnable.setStatus("current")


class _BoxServicesPSMStateTrapEnable_Type(Integer32):
    """Custom type boxServicesPSMStateTrapEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_BoxServicesPSMStateTrapEnable_Type.__name__ = "Integer32"
_BoxServicesPSMStateTrapEnable_Object = MibScalar
boxServicesPSMStateTrapEnable = _BoxServicesPSMStateTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 4),
    _BoxServicesPSMStateTrapEnable_Type()
)
boxServicesPSMStateTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boxServicesPSMStateTrapEnable.setStatus("current")


class _BoxServicesFanStateTrapEnable_Type(Integer32):
    """Custom type boxServicesFanStateTrapEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_BoxServicesFanStateTrapEnable_Type.__name__ = "Integer32"
_BoxServicesFanStateTrapEnable_Object = MibScalar
boxServicesFanStateTrapEnable = _BoxServicesFanStateTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 5),
    _BoxServicesFanStateTrapEnable_Type()
)
boxServicesFanStateTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boxServicesFanStateTrapEnable.setStatus("current")
_BoxServicesFansTable_Object = MibTable
boxServicesFansTable = _BoxServicesFansTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 6)
)
if mibBuilder.loadTexts:
    boxServicesFansTable.setStatus("current")
_BoxServicesFansEntry_Object = MibTableRow
boxServicesFansEntry = _BoxServicesFansEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 6, 1)
)
boxServicesFansEntry.setIndexNames(
    (0, "DNOS-BOXSERVICES-PRIVATE-MIB", "boxServicesFanUnitIndex"),
    (0, "DNOS-BOXSERVICES-PRIVATE-MIB", "boxServicesFansIndex"),
)
if mibBuilder.loadTexts:
    boxServicesFansEntry.setStatus("current")


class _BoxServicesFansIndex_Type(Integer32):
    """Custom type boxServicesFansIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BoxServicesFansIndex_Type.__name__ = "Integer32"
_BoxServicesFansIndex_Object = MibTableColumn
boxServicesFansIndex = _BoxServicesFansIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 6, 1, 1),
    _BoxServicesFansIndex_Type()
)
boxServicesFansIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesFansIndex.setStatus("current")


class _BoxServicesFanItemType_Type(Integer32):
    """Custom type boxServicesFanItemType based on Integer32"""
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
        *(("fixed", 1),
          ("removable", 2),
          ("fixedAC", 3),
          ("removableDC", 4),
          ("fixedDC", 5),
          ("removableAC", 6))
    )


_BoxServicesFanItemType_Type.__name__ = "Integer32"
_BoxServicesFanItemType_Object = MibTableColumn
boxServicesFanItemType = _BoxServicesFanItemType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 6, 1, 2),
    _BoxServicesFanItemType_Type()
)
boxServicesFanItemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesFanItemType.setStatus("current")


class _BoxServicesFanItemState_Type(Integer32):
    """Custom type boxServicesFanItemState based on Integer32"""
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
        *(("notpresent", 1),
          ("operational", 2),
          ("failed", 3),
          ("powering", 4),
          ("nopower", 5),
          ("notpowering", 6),
          ("incompatible", 7))
    )


_BoxServicesFanItemState_Type.__name__ = "Integer32"
_BoxServicesFanItemState_Object = MibTableColumn
boxServicesFanItemState = _BoxServicesFanItemState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 6, 1, 3),
    _BoxServicesFanItemState_Type()
)
boxServicesFanItemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesFanItemState.setStatus("current")
_BoxServicesFanSpeed_Type = Integer32
_BoxServicesFanSpeed_Object = MibTableColumn
boxServicesFanSpeed = _BoxServicesFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 6, 1, 4),
    _BoxServicesFanSpeed_Type()
)
boxServicesFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesFanSpeed.setStatus("current")
_BoxServicesFanDutyLevel_Type = Integer32
_BoxServicesFanDutyLevel_Object = MibTableColumn
boxServicesFanDutyLevel = _BoxServicesFanDutyLevel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 6, 1, 5),
    _BoxServicesFanDutyLevel_Type()
)
boxServicesFanDutyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesFanDutyLevel.setStatus("current")
_BoxServicesFanUnitIndex_Type = Unsigned32
_BoxServicesFanUnitIndex_Object = MibTableColumn
boxServicesFanUnitIndex = _BoxServicesFanUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 6, 1, 6),
    _BoxServicesFanUnitIndex_Type()
)
boxServicesFanUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesFanUnitIndex.setStatus("current")
_BoxServicesPowSuppliesTable_Object = MibTable
boxServicesPowSuppliesTable = _BoxServicesPowSuppliesTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 7)
)
if mibBuilder.loadTexts:
    boxServicesPowSuppliesTable.setStatus("current")
_BoxServicesPowSuppliesEntry_Object = MibTableRow
boxServicesPowSuppliesEntry = _BoxServicesPowSuppliesEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 7, 1)
)
boxServicesPowSuppliesEntry.setIndexNames(
    (0, "DNOS-BOXSERVICES-PRIVATE-MIB", "boxServicesPowerSuppUnitIndex"),
    (0, "DNOS-BOXSERVICES-PRIVATE-MIB", "boxServicesPowSupplyIndex"),
)
if mibBuilder.loadTexts:
    boxServicesPowSuppliesEntry.setStatus("current")


class _BoxServicesPowSupplyIndex_Type(Integer32):
    """Custom type boxServicesPowSupplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BoxServicesPowSupplyIndex_Type.__name__ = "Integer32"
_BoxServicesPowSupplyIndex_Object = MibTableColumn
boxServicesPowSupplyIndex = _BoxServicesPowSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 7, 1, 1),
    _BoxServicesPowSupplyIndex_Type()
)
boxServicesPowSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesPowSupplyIndex.setStatus("current")


class _BoxServicesPowSupplyItemType_Type(Integer32):
    """Custom type boxServicesPowSupplyItemType based on Integer32"""
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
        *(("fixed", 1),
          ("removable", 2),
          ("fixedAC", 3),
          ("removableDC", 4),
          ("fixedDC", 5),
          ("removableAC", 6))
    )


_BoxServicesPowSupplyItemType_Type.__name__ = "Integer32"
_BoxServicesPowSupplyItemType_Object = MibTableColumn
boxServicesPowSupplyItemType = _BoxServicesPowSupplyItemType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 7, 1, 2),
    _BoxServicesPowSupplyItemType_Type()
)
boxServicesPowSupplyItemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesPowSupplyItemType.setStatus("current")


class _BoxServicesPowSupplyItemState_Type(Integer32):
    """Custom type boxServicesPowSupplyItemState based on Integer32"""
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
        *(("notpresent", 1),
          ("operational", 2),
          ("failed", 3),
          ("powering", 4),
          ("nopower", 5),
          ("notpowering", 6),
          ("incompatible", 7))
    )


_BoxServicesPowSupplyItemState_Type.__name__ = "Integer32"
_BoxServicesPowSupplyItemState_Object = MibTableColumn
boxServicesPowSupplyItemState = _BoxServicesPowSupplyItemState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 7, 1, 3),
    _BoxServicesPowSupplyItemState_Type()
)
boxServicesPowSupplyItemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesPowSupplyItemState.setStatus("current")
_BoxServicesPowerSuppUnitIndex_Type = Unsigned32
_BoxServicesPowerSuppUnitIndex_Object = MibTableColumn
boxServicesPowerSuppUnitIndex = _BoxServicesPowerSuppUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 7, 1, 4),
    _BoxServicesPowerSuppUnitIndex_Type()
)
boxServicesPowerSuppUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesPowerSuppUnitIndex.setStatus("current")
_BoxServicesTempSensorsTable_Object = MibTable
boxServicesTempSensorsTable = _BoxServicesTempSensorsTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 8)
)
if mibBuilder.loadTexts:
    boxServicesTempSensorsTable.setStatus("current")
_BoxServicesTempSensorsEntry_Object = MibTableRow
boxServicesTempSensorsEntry = _BoxServicesTempSensorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 8, 1)
)
boxServicesTempSensorsEntry.setIndexNames(
    (0, "DNOS-BOXSERVICES-PRIVATE-MIB", "boxServicesUnitIndex"),
    (0, "DNOS-BOXSERVICES-PRIVATE-MIB", "boxServicesTempSensorIndex"),
)
if mibBuilder.loadTexts:
    boxServicesTempSensorsEntry.setStatus("current")
_BoxServicesUnitIndex_Type = Unsigned32
_BoxServicesUnitIndex_Object = MibTableColumn
boxServicesUnitIndex = _BoxServicesUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 8, 1, 1),
    _BoxServicesUnitIndex_Type()
)
boxServicesUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesUnitIndex.setStatus("current")
_BoxServicesTempSensorIndex_Type = Unsigned32
_BoxServicesTempSensorIndex_Object = MibTableColumn
boxServicesTempSensorIndex = _BoxServicesTempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 8, 1, 2),
    _BoxServicesTempSensorIndex_Type()
)
boxServicesTempSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesTempSensorIndex.setStatus("current")


class _BoxServicesTempSensorType_Type(Integer32):
    """Custom type boxServicesTempSensorType based on Integer32"""
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
        *(("fixed", 1),
          ("removable", 2),
          ("fixedAC", 3),
          ("removableDC", 4),
          ("fixedDC", 5),
          ("removableAC", 6))
    )


_BoxServicesTempSensorType_Type.__name__ = "Integer32"
_BoxServicesTempSensorType_Object = MibTableColumn
boxServicesTempSensorType = _BoxServicesTempSensorType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 8, 1, 3),
    _BoxServicesTempSensorType_Type()
)
boxServicesTempSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesTempSensorType.setStatus("current")
_BoxServicesTempSensorState_Type = BoxsTemperatureStatus
_BoxServicesTempSensorState_Object = MibTableColumn
boxServicesTempSensorState = _BoxServicesTempSensorState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 8, 1, 4),
    _BoxServicesTempSensorState_Type()
)
boxServicesTempSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesTempSensorState.setStatus("obsolete")
_BoxServicesTempSensorTemperature_Type = Integer32
_BoxServicesTempSensorTemperature_Object = MibTableColumn
boxServicesTempSensorTemperature = _BoxServicesTempSensorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 8, 1, 5),
    _BoxServicesTempSensorTemperature_Type()
)
boxServicesTempSensorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesTempSensorTemperature.setStatus("current")
_BoxsUnitPwrUsageHistoryTable_Object = MibTable
boxsUnitPwrUsageHistoryTable = _BoxsUnitPwrUsageHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 9)
)
if mibBuilder.loadTexts:
    boxsUnitPwrUsageHistoryTable.setStatus("current")
_BoxsUnitPwrUsageHistoryEntry_Object = MibTableRow
boxsUnitPwrUsageHistoryEntry = _BoxsUnitPwrUsageHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 9, 1)
)
boxsUnitPwrUsageHistoryEntry.setIndexNames(
    (0, "DNOS-BOXSERVICES-PRIVATE-MIB", "boxsPwrUsageHistoryUnitIndex"),
    (0, "DNOS-BOXSERVICES-PRIVATE-MIB", "boxsPwrUsageHistoryUnitSampleIndex"),
)
if mibBuilder.loadTexts:
    boxsUnitPwrUsageHistoryEntry.setStatus("current")


class _BoxsPwrUsageHistoryUnitIndex_Type(Integer32):
    """Custom type boxsPwrUsageHistoryUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BoxsPwrUsageHistoryUnitIndex_Type.__name__ = "Integer32"
_BoxsPwrUsageHistoryUnitIndex_Object = MibTableColumn
boxsPwrUsageHistoryUnitIndex = _BoxsPwrUsageHistoryUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 9, 1, 1),
    _BoxsPwrUsageHistoryUnitIndex_Type()
)
boxsPwrUsageHistoryUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    boxsPwrUsageHistoryUnitIndex.setStatus("current")


class _BoxsPwrUsageHistoryUnitSampleIndex_Type(Integer32):
    """Custom type boxsPwrUsageHistoryUnitSampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BoxsPwrUsageHistoryUnitSampleIndex_Type.__name__ = "Integer32"
_BoxsPwrUsageHistoryUnitSampleIndex_Object = MibTableColumn
boxsPwrUsageHistoryUnitSampleIndex = _BoxsPwrUsageHistoryUnitSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 9, 1, 2),
    _BoxsPwrUsageHistoryUnitSampleIndex_Type()
)
boxsPwrUsageHistoryUnitSampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    boxsPwrUsageHistoryUnitSampleIndex.setStatus("current")


class _BoxsPwrUsageHistoryUnitSampleTime_Type(DisplayString):
    """Custom type boxsPwrUsageHistoryUnitSampleTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BoxsPwrUsageHistoryUnitSampleTime_Type.__name__ = "DisplayString"
_BoxsPwrUsageHistoryUnitSampleTime_Object = MibTableColumn
boxsPwrUsageHistoryUnitSampleTime = _BoxsPwrUsageHistoryUnitSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 9, 1, 3),
    _BoxsPwrUsageHistoryUnitSampleTime_Type()
)
boxsPwrUsageHistoryUnitSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxsPwrUsageHistoryUnitSampleTime.setStatus("current")
_BoxsPwrUsageHistoryUnitPowerConsumption_Type = Integer32
_BoxsPwrUsageHistoryUnitPowerConsumption_Object = MibTableColumn
boxsPwrUsageHistoryUnitPowerConsumption = _BoxsPwrUsageHistoryUnitPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 9, 1, 4),
    _BoxsPwrUsageHistoryUnitPowerConsumption_Type()
)
boxsPwrUsageHistoryUnitPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxsPwrUsageHistoryUnitPowerConsumption.setStatus("current")
_BoxsPwrUsageHistoryStackPowerConsumption_Type = Integer32
_BoxsPwrUsageHistoryStackPowerConsumption_Object = MibTableColumn
boxsPwrUsageHistoryStackPowerConsumption = _BoxsPwrUsageHistoryStackPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 9, 1, 5),
    _BoxsPwrUsageHistoryStackPowerConsumption_Type()
)
boxsPwrUsageHistoryStackPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxsPwrUsageHistoryStackPowerConsumption.setStatus("current")


class _BoxsPwrUsageHistoryUnitSampleInterval_Type(Integer32):
    """Custom type boxsPwrUsageHistoryUnitSampleInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 86400),
    )


_BoxsPwrUsageHistoryUnitSampleInterval_Type.__name__ = "Integer32"
_BoxsPwrUsageHistoryUnitSampleInterval_Object = MibScalar
boxsPwrUsageHistoryUnitSampleInterval = _BoxsPwrUsageHistoryUnitSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 10),
    _BoxsPwrUsageHistoryUnitSampleInterval_Type()
)
boxsPwrUsageHistoryUnitSampleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boxsPwrUsageHistoryUnitSampleInterval.setStatus("current")


class _BoxsPwrUsageHistoryUnitMaxSamples_Type(Integer32):
    """Custom type boxsPwrUsageHistoryUnitMaxSamples based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 168),
    )


_BoxsPwrUsageHistoryUnitMaxSamples_Type.__name__ = "Integer32"
_BoxsPwrUsageHistoryUnitMaxSamples_Object = MibScalar
boxsPwrUsageHistoryUnitMaxSamples = _BoxsPwrUsageHistoryUnitMaxSamples_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 11),
    _BoxsPwrUsageHistoryUnitMaxSamples_Type()
)
boxsPwrUsageHistoryUnitMaxSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boxsPwrUsageHistoryUnitMaxSamples.setStatus("current")
_BoxServicesThermalShutdownSensor_Type = Unsigned32
_BoxServicesThermalShutdownSensor_Object = MibScalar
boxServicesThermalShutdownSensor = _BoxServicesThermalShutdownSensor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 13),
    _BoxServicesThermalShutdownSensor_Type()
)
boxServicesThermalShutdownSensor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    boxServicesThermalShutdownSensor.setStatus("current")
_BoxServicesThermalShutdownTemperature_Type = Unsigned32
_BoxServicesThermalShutdownTemperature_Object = MibScalar
boxServicesThermalShutdownTemperature = _BoxServicesThermalShutdownTemperature_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 14),
    _BoxServicesThermalShutdownTemperature_Type()
)
boxServicesThermalShutdownTemperature.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    boxServicesThermalShutdownTemperature.setStatus("current")
_BoxServicesTempUnitTable_Object = MibTable
boxServicesTempUnitTable = _BoxServicesTempUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 15)
)
if mibBuilder.loadTexts:
    boxServicesTempUnitTable.setStatus("current")
_BoxServicesTempUnitEntry_Object = MibTableRow
boxServicesTempUnitEntry = _BoxServicesTempUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 15, 1)
)
boxServicesTempUnitEntry.setIndexNames(
    (0, "DNOS-BOXSERVICES-PRIVATE-MIB", "boxServicesTempUnitIndex"),
)
if mibBuilder.loadTexts:
    boxServicesTempUnitEntry.setStatus("current")
_BoxServicesTempUnitIndex_Type = Unsigned32
_BoxServicesTempUnitIndex_Object = MibTableColumn
boxServicesTempUnitIndex = _BoxServicesTempUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 15, 1, 1),
    _BoxServicesTempUnitIndex_Type()
)
boxServicesTempUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesTempUnitIndex.setStatus("current")
_BoxServicesTempUnitState_Type = BoxsTemperatureStatus
_BoxServicesTempUnitState_Object = MibTableColumn
boxServicesTempUnitState = _BoxServicesTempUnitState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 15, 1, 2),
    _BoxServicesTempUnitState_Type()
)
boxServicesTempUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesTempUnitState.setStatus("current")
_BoxServicesTempUnitTemperature_Type = Integer32
_BoxServicesTempUnitTemperature_Object = MibTableColumn
boxServicesTempUnitTemperature = _BoxServicesTempUnitTemperature_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 15, 1, 3),
    _BoxServicesTempUnitTemperature_Type()
)
boxServicesTempUnitTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boxServicesTempUnitTemperature.setStatus("current")
_BoxServicesNotificationsGroup_ObjectIdentity = ObjectIdentity
boxServicesNotificationsGroup = _BoxServicesNotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 2)
)


class _BoxsItemStateChangeEvent_Type(Integer32):
    """Custom type boxsItemStateChangeEvent based on Integer32"""
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
        *(("insertion", 1),
          ("removal", 2),
          ("becomeoperational", 3),
          ("failure", 4),
          ("losepower", 5))
    )


_BoxsItemStateChangeEvent_Type.__name__ = "Integer32"
_BoxsItemStateChangeEvent_Object = MibScalar
boxsItemStateChangeEvent = _BoxsItemStateChangeEvent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 2, 1),
    _BoxsItemStateChangeEvent_Type()
)
boxsItemStateChangeEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    boxsItemStateChangeEvent.setStatus("current")


class _BoxsTemperatureChangeEvent_Type(Integer32):
    """Custom type boxsTemperatureChangeEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("abovethreshold", 1),
          ("belowthreshold", 2),
          ("withinnormalrange", 3))
    )


_BoxsTemperatureChangeEvent_Type.__name__ = "Integer32"
_BoxsTemperatureChangeEvent_Object = MibScalar
boxsTemperatureChangeEvent = _BoxsTemperatureChangeEvent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 2, 2),
    _BoxsTemperatureChangeEvent_Type()
)
boxsTemperatureChangeEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    boxsTemperatureChangeEvent.setStatus("current")
_BoxsTemperatureStatusCurrentEvent_Type = BoxsTemperatureStatus
_BoxsTemperatureStatusCurrentEvent_Object = MibScalar
boxsTemperatureStatusCurrentEvent = _BoxsTemperatureStatusCurrentEvent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 2, 3),
    _BoxsTemperatureStatusCurrentEvent_Type()
)
boxsTemperatureStatusCurrentEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    boxsTemperatureStatusCurrentEvent.setStatus("current")
_BoxsTemperatureStatusPreviousEvent_Type = BoxsTemperatureStatus
_BoxsTemperatureStatusPreviousEvent_Object = MibScalar
boxsTemperatureStatusPreviousEvent = _BoxsTemperatureStatusPreviousEvent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 2, 4),
    _BoxsTemperatureStatusPreviousEvent_Type()
)
boxsTemperatureStatusPreviousEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    boxsTemperatureStatusPreviousEvent.setStatus("current")
_BoxsLocatorLedConfigGroup_ObjectIdentity = ObjectIdentity
boxsLocatorLedConfigGroup = _BoxsLocatorLedConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 4)
)
_BoxsLocatorLedUnit_Type = Integer32
_BoxsLocatorLedUnit_Object = MibScalar
boxsLocatorLedUnit = _BoxsLocatorLedUnit_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 4, 1),
    _BoxsLocatorLedUnit_Type()
)
boxsLocatorLedUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boxsLocatorLedUnit.setStatus("current")


class _BoxsLocatorLedTime_Type(Integer32):
    """Custom type boxsLocatorLedTime based on Integer32"""
    defaultValue = 20


_BoxsLocatorLedTime_Type.__name__ = "Integer32"
_BoxsLocatorLedTime_Object = MibScalar
boxsLocatorLedTime = _BoxsLocatorLedTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 4, 2),
    _BoxsLocatorLedTime_Type()
)
boxsLocatorLedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boxsLocatorLedTime.setStatus("current")


class _BoxsLocatorLedEnable_Type(Integer32):
    """Custom type boxsLocatorLedEnable based on Integer32"""
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


_BoxsLocatorLedEnable_Type.__name__ = "Integer32"
_BoxsLocatorLedEnable_Object = MibScalar
boxsLocatorLedEnable = _BoxsLocatorLedEnable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 4, 3),
    _BoxsLocatorLedEnable_Type()
)
boxsLocatorLedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boxsLocatorLedEnable.setStatus("current")

# Managed Objects groups


# Notification objects

boxsFanStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 0, 1)
)
boxsFanStateChange.setObjects(
      *(("DNOS-BOXSERVICES-PRIVATE-MIB", "boxServicesFansIndex"),
        ("DNOS-BOXSERVICES-PRIVATE-MIB", "boxsItemStateChangeEvent"))
)
if mibBuilder.loadTexts:
    boxsFanStateChange.setStatus(
        "current"
    )

boxsPowSupplyStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 0, 2)
)
boxsPowSupplyStateChange.setObjects(
      *(("DNOS-BOXSERVICES-PRIVATE-MIB", "boxServicesPowSupplyIndex"),
        ("DNOS-BOXSERVICES-PRIVATE-MIB", "boxsItemStateChangeEvent"))
)
if mibBuilder.loadTexts:
    boxsPowSupplyStateChange.setStatus(
        "current"
    )

boxsTemperatureChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 0, 3)
)
boxsTemperatureChange.setObjects(
      *(("DNOS-BOXSERVICES-PRIVATE-MIB", "boxServicesTempSensorIndex"),
        ("DNOS-BOXSERVICES-PRIVATE-MIB", "boxsTemperatureChangeEvent"))
)
if mibBuilder.loadTexts:
    boxsTemperatureChange.setStatus(
        "obsolete"
    )

boxsThermalShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 0, 4)
)
boxsThermalShutdown.setObjects(
      *(("DNOS-BOXSERVICES-PRIVATE-MIB", "boxServicesThermalShutdownSensor"),
        ("DNOS-BOXSERVICES-PRIVATE-MIB", "boxServicesThermalShutdownTemperature"))
)
if mibBuilder.loadTexts:
    boxsThermalShutdown.setStatus(
        "current"
    )

boxsTemperatureStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 0, 5)
)
boxsTemperatureStateChange.setObjects(
      *(("DNOS-BOXSERVICES-PRIVATE-MIB", "boxServicesTempUnitIndex"),
        ("DNOS-BOXSERVICES-PRIVATE-MIB", "boxsTemperatureStatusCurrentEvent"),
        ("DNOS-BOXSERVICES-PRIVATE-MIB", "boxsTemperatureStatusPreviousEvent"))
)
if mibBuilder.loadTexts:
    boxsTemperatureStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-BOXSERVICES-PRIVATE-MIB",
    **{"BoxsTemperatureStatus": BoxsTemperatureStatus,
       "fastPathBoxServices": fastPathBoxServices,
       "fastPathBoxServicesTraps": fastPathBoxServicesTraps,
       "boxsFanStateChange": boxsFanStateChange,
       "boxsPowSupplyStateChange": boxsPowSupplyStateChange,
       "boxsTemperatureChange": boxsTemperatureChange,
       "boxsThermalShutdown": boxsThermalShutdown,
       "boxsTemperatureStateChange": boxsTemperatureStateChange,
       "boxServicesGroup": boxServicesGroup,
       "boxServicesNormalTempRangeMin": boxServicesNormalTempRangeMin,
       "boxServicesNormalTempRangeMax": boxServicesNormalTempRangeMax,
       "boxServicesTemperatureTrapEnable": boxServicesTemperatureTrapEnable,
       "boxServicesPSMStateTrapEnable": boxServicesPSMStateTrapEnable,
       "boxServicesFanStateTrapEnable": boxServicesFanStateTrapEnable,
       "boxServicesFansTable": boxServicesFansTable,
       "boxServicesFansEntry": boxServicesFansEntry,
       "boxServicesFansIndex": boxServicesFansIndex,
       "boxServicesFanItemType": boxServicesFanItemType,
       "boxServicesFanItemState": boxServicesFanItemState,
       "boxServicesFanSpeed": boxServicesFanSpeed,
       "boxServicesFanDutyLevel": boxServicesFanDutyLevel,
       "boxServicesFanUnitIndex": boxServicesFanUnitIndex,
       "boxServicesPowSuppliesTable": boxServicesPowSuppliesTable,
       "boxServicesPowSuppliesEntry": boxServicesPowSuppliesEntry,
       "boxServicesPowSupplyIndex": boxServicesPowSupplyIndex,
       "boxServicesPowSupplyItemType": boxServicesPowSupplyItemType,
       "boxServicesPowSupplyItemState": boxServicesPowSupplyItemState,
       "boxServicesPowerSuppUnitIndex": boxServicesPowerSuppUnitIndex,
       "boxServicesTempSensorsTable": boxServicesTempSensorsTable,
       "boxServicesTempSensorsEntry": boxServicesTempSensorsEntry,
       "boxServicesUnitIndex": boxServicesUnitIndex,
       "boxServicesTempSensorIndex": boxServicesTempSensorIndex,
       "boxServicesTempSensorType": boxServicesTempSensorType,
       "boxServicesTempSensorState": boxServicesTempSensorState,
       "boxServicesTempSensorTemperature": boxServicesTempSensorTemperature,
       "boxsUnitPwrUsageHistoryTable": boxsUnitPwrUsageHistoryTable,
       "boxsUnitPwrUsageHistoryEntry": boxsUnitPwrUsageHistoryEntry,
       "boxsPwrUsageHistoryUnitIndex": boxsPwrUsageHistoryUnitIndex,
       "boxsPwrUsageHistoryUnitSampleIndex": boxsPwrUsageHistoryUnitSampleIndex,
       "boxsPwrUsageHistoryUnitSampleTime": boxsPwrUsageHistoryUnitSampleTime,
       "boxsPwrUsageHistoryUnitPowerConsumption": boxsPwrUsageHistoryUnitPowerConsumption,
       "boxsPwrUsageHistoryStackPowerConsumption": boxsPwrUsageHistoryStackPowerConsumption,
       "boxsPwrUsageHistoryUnitSampleInterval": boxsPwrUsageHistoryUnitSampleInterval,
       "boxsPwrUsageHistoryUnitMaxSamples": boxsPwrUsageHistoryUnitMaxSamples,
       "boxServicesThermalShutdownSensor": boxServicesThermalShutdownSensor,
       "boxServicesThermalShutdownTemperature": boxServicesThermalShutdownTemperature,
       "boxServicesTempUnitTable": boxServicesTempUnitTable,
       "boxServicesTempUnitEntry": boxServicesTempUnitEntry,
       "boxServicesTempUnitIndex": boxServicesTempUnitIndex,
       "boxServicesTempUnitState": boxServicesTempUnitState,
       "boxServicesTempUnitTemperature": boxServicesTempUnitTemperature,
       "boxServicesNotificationsGroup": boxServicesNotificationsGroup,
       "boxsItemStateChangeEvent": boxsItemStateChangeEvent,
       "boxsTemperatureChangeEvent": boxsTemperatureChangeEvent,
       "boxsTemperatureStatusCurrentEvent": boxsTemperatureStatusCurrentEvent,
       "boxsTemperatureStatusPreviousEvent": boxsTemperatureStatusPreviousEvent,
       "boxsLocatorLedConfigGroup": boxsLocatorLedConfigGroup,
       "boxsLocatorLedUnit": boxsLocatorLedUnit,
       "boxsLocatorLedTime": boxsLocatorLedTime,
       "boxsLocatorLedEnable": boxsLocatorLedEnable}
)
