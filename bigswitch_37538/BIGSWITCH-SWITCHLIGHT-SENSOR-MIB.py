# SNMP MIB module (BIGSWITCH-SWITCHLIGHT-SENSOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/bigswitch_37538/BIGSWITCH-SWITCHLIGHT-SENSOR-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:48:03 2025
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

(bsn,) = mibBuilder.importSymbols(
    "BIGSWITCH-MIB",
    "bsn")

(bsnSwitchlight,) = mibBuilder.importSymbols(
    "BIGSWITCH-SWITCHLIGHT-MIB",
    "bsnSwitchlight")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

slSensors = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3)
)
if mibBuilder.loadTexts:
    slSensors.setRevisions(
        ("2014-04-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SlTempSensorsTable_Object = MibTable
slTempSensorsTable = _SlTempSensorsTable_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 1)
)
if mibBuilder.loadTexts:
    slTempSensorsTable.setStatus("current")
_SlTempSensorsEntry_Object = MibTableRow
slTempSensorsEntry = _SlTempSensorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 1, 1)
)
slTempSensorsEntry.setIndexNames(
    (0, "BIGSWITCH-SWITCHLIGHT-SENSOR-MIB", "slTempSensorsIndex"),
)
if mibBuilder.loadTexts:
    slTempSensorsEntry.setStatus("current")


class _SlTempSensorsIndex_Type(Integer32):
    """Custom type slTempSensorsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlTempSensorsIndex_Type.__name__ = "Integer32"
_SlTempSensorsIndex_Object = MibTableColumn
slTempSensorsIndex = _SlTempSensorsIndex_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 1, 1, 1),
    _SlTempSensorsIndex_Type()
)
slTempSensorsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slTempSensorsIndex.setStatus("current")
_SlTempSensorsDevice_Type = DisplayString
_SlTempSensorsDevice_Object = MibTableColumn
slTempSensorsDevice = _SlTempSensorsDevice_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 1, 1, 2),
    _SlTempSensorsDevice_Type()
)
slTempSensorsDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slTempSensorsDevice.setStatus("current")


class _SlTempSensorsStatus_Type(Integer32):
    """Custom type slTempSensorsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("missing", 0),
          ("good", 1),
          ("failed", 2))
    )


_SlTempSensorsStatus_Type.__name__ = "Integer32"
_SlTempSensorsStatus_Object = MibTableColumn
slTempSensorsStatus = _SlTempSensorsStatus_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 1, 1, 3),
    _SlTempSensorsStatus_Type()
)
slTempSensorsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slTempSensorsStatus.setStatus("current")
_SlTempSensorsValue_Type = Gauge32
_SlTempSensorsValue_Object = MibTableColumn
slTempSensorsValue = _SlTempSensorsValue_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 1, 1, 4),
    _SlTempSensorsValue_Type()
)
slTempSensorsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slTempSensorsValue.setStatus("current")
_SlFanSensorsTable_Object = MibTable
slFanSensorsTable = _SlFanSensorsTable_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 2)
)
if mibBuilder.loadTexts:
    slFanSensorsTable.setStatus("current")
_SlFanSensorsEntry_Object = MibTableRow
slFanSensorsEntry = _SlFanSensorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 2, 1)
)
slFanSensorsEntry.setIndexNames(
    (0, "BIGSWITCH-SWITCHLIGHT-SENSOR-MIB", "slFanSensorsIndex"),
)
if mibBuilder.loadTexts:
    slFanSensorsEntry.setStatus("current")


class _SlFanSensorsIndex_Type(Integer32):
    """Custom type slFanSensorsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlFanSensorsIndex_Type.__name__ = "Integer32"
_SlFanSensorsIndex_Object = MibTableColumn
slFanSensorsIndex = _SlFanSensorsIndex_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 2, 1, 1),
    _SlFanSensorsIndex_Type()
)
slFanSensorsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slFanSensorsIndex.setStatus("current")
_SlFanSensorsDevice_Type = DisplayString
_SlFanSensorsDevice_Object = MibTableColumn
slFanSensorsDevice = _SlFanSensorsDevice_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 2, 1, 2),
    _SlFanSensorsDevice_Type()
)
slFanSensorsDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slFanSensorsDevice.setStatus("current")


class _SlFanSensorsStatus_Type(Integer32):
    """Custom type slFanSensorsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("missing", 0),
          ("good", 1),
          ("failed", 2))
    )


_SlFanSensorsStatus_Type.__name__ = "Integer32"
_SlFanSensorsStatus_Object = MibTableColumn
slFanSensorsStatus = _SlFanSensorsStatus_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 2, 1, 3),
    _SlFanSensorsStatus_Type()
)
slFanSensorsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slFanSensorsStatus.setStatus("current")
_SlFanSensorsFlowType_Type = DisplayString
_SlFanSensorsFlowType_Object = MibTableColumn
slFanSensorsFlowType = _SlFanSensorsFlowType_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 2, 1, 4),
    _SlFanSensorsFlowType_Type()
)
slFanSensorsFlowType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slFanSensorsFlowType.setStatus("current")
_SlFanSensorsRPM_Type = Gauge32
_SlFanSensorsRPM_Object = MibTableColumn
slFanSensorsRPM = _SlFanSensorsRPM_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 2, 1, 5),
    _SlFanSensorsRPM_Type()
)
slFanSensorsRPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slFanSensorsRPM.setStatus("current")
_SlFanSensorsPct_Type = Gauge32
_SlFanSensorsPct_Object = MibTableColumn
slFanSensorsPct = _SlFanSensorsPct_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 2, 1, 6),
    _SlFanSensorsPct_Type()
)
slFanSensorsPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slFanSensorsPct.setStatus("current")
_SlPSUSensorsTable_Object = MibTable
slPSUSensorsTable = _SlPSUSensorsTable_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 3)
)
if mibBuilder.loadTexts:
    slPSUSensorsTable.setStatus("current")
_SlPSUSensorsEntry_Object = MibTableRow
slPSUSensorsEntry = _SlPSUSensorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 3, 1)
)
slPSUSensorsEntry.setIndexNames(
    (0, "BIGSWITCH-SWITCHLIGHT-SENSOR-MIB", "slPSUSensorsIndex"),
)
if mibBuilder.loadTexts:
    slPSUSensorsEntry.setStatus("current")


class _SlPSUSensorsIndex_Type(Integer32):
    """Custom type slPSUSensorsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlPSUSensorsIndex_Type.__name__ = "Integer32"
_SlPSUSensorsIndex_Object = MibTableColumn
slPSUSensorsIndex = _SlPSUSensorsIndex_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 3, 1, 1),
    _SlPSUSensorsIndex_Type()
)
slPSUSensorsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPSUSensorsIndex.setStatus("current")
_SlPSUSensorsDevice_Type = DisplayString
_SlPSUSensorsDevice_Object = MibTableColumn
slPSUSensorsDevice = _SlPSUSensorsDevice_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 3, 1, 2),
    _SlPSUSensorsDevice_Type()
)
slPSUSensorsDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPSUSensorsDevice.setStatus("current")


class _SlPSUSensorsStatus_Type(Integer32):
    """Custom type slPSUSensorsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("missing", 0),
          ("good", 1),
          ("failed", 2))
    )


_SlPSUSensorsStatus_Type.__name__ = "Integer32"
_SlPSUSensorsStatus_Object = MibTableColumn
slPSUSensorsStatus = _SlPSUSensorsStatus_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 3, 1, 3),
    _SlPSUSensorsStatus_Type()
)
slPSUSensorsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPSUSensorsStatus.setStatus("current")
_SlPSUSensorsCurrentType_Type = DisplayString
_SlPSUSensorsCurrentType_Object = MibTableColumn
slPSUSensorsCurrentType = _SlPSUSensorsCurrentType_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 3, 1, 4),
    _SlPSUSensorsCurrentType_Type()
)
slPSUSensorsCurrentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPSUSensorsCurrentType.setStatus("current")
_SlPSUSensorsModel_Type = DisplayString
_SlPSUSensorsModel_Object = MibTableColumn
slPSUSensorsModel = _SlPSUSensorsModel_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 3, 1, 5),
    _SlPSUSensorsModel_Type()
)
slPSUSensorsModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPSUSensorsModel.setStatus("current")
_SlPSUSensorsVin_Type = Gauge32
_SlPSUSensorsVin_Object = MibTableColumn
slPSUSensorsVin = _SlPSUSensorsVin_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 3, 1, 6),
    _SlPSUSensorsVin_Type()
)
slPSUSensorsVin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPSUSensorsVin.setStatus("current")
_SlPSUSensorsVout_Type = Gauge32
_SlPSUSensorsVout_Object = MibTableColumn
slPSUSensorsVout = _SlPSUSensorsVout_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 3, 1, 7),
    _SlPSUSensorsVout_Type()
)
slPSUSensorsVout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPSUSensorsVout.setStatus("current")
_SlPSUSensorsIin_Type = Gauge32
_SlPSUSensorsIin_Object = MibTableColumn
slPSUSensorsIin = _SlPSUSensorsIin_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 3, 1, 8),
    _SlPSUSensorsIin_Type()
)
slPSUSensorsIin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPSUSensorsIin.setStatus("current")
_SlPSUSensorsIout_Type = Gauge32
_SlPSUSensorsIout_Object = MibTableColumn
slPSUSensorsIout = _SlPSUSensorsIout_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 3, 1, 9),
    _SlPSUSensorsIout_Type()
)
slPSUSensorsIout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPSUSensorsIout.setStatus("current")
_SlPSUSensorsPin_Type = Gauge32
_SlPSUSensorsPin_Object = MibTableColumn
slPSUSensorsPin = _SlPSUSensorsPin_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 3, 1, 10),
    _SlPSUSensorsPin_Type()
)
slPSUSensorsPin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPSUSensorsPin.setStatus("current")
_SlPSUSensorsPout_Type = Gauge32
_SlPSUSensorsPout_Object = MibTableColumn
slPSUSensorsPout = _SlPSUSensorsPout_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 3, 3, 1, 11),
    _SlPSUSensorsPout_Type()
)
slPSUSensorsPout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slPSUSensorsPout.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIGSWITCH-SWITCHLIGHT-SENSOR-MIB",
    **{"slSensors": slSensors,
       "slTempSensorsTable": slTempSensorsTable,
       "slTempSensorsEntry": slTempSensorsEntry,
       "slTempSensorsIndex": slTempSensorsIndex,
       "slTempSensorsDevice": slTempSensorsDevice,
       "slTempSensorsStatus": slTempSensorsStatus,
       "slTempSensorsValue": slTempSensorsValue,
       "slFanSensorsTable": slFanSensorsTable,
       "slFanSensorsEntry": slFanSensorsEntry,
       "slFanSensorsIndex": slFanSensorsIndex,
       "slFanSensorsDevice": slFanSensorsDevice,
       "slFanSensorsStatus": slFanSensorsStatus,
       "slFanSensorsFlowType": slFanSensorsFlowType,
       "slFanSensorsRPM": slFanSensorsRPM,
       "slFanSensorsPct": slFanSensorsPct,
       "slPSUSensorsTable": slPSUSensorsTable,
       "slPSUSensorsEntry": slPSUSensorsEntry,
       "slPSUSensorsIndex": slPSUSensorsIndex,
       "slPSUSensorsDevice": slPSUSensorsDevice,
       "slPSUSensorsStatus": slPSUSensorsStatus,
       "slPSUSensorsCurrentType": slPSUSensorsCurrentType,
       "slPSUSensorsModel": slPSUSensorsModel,
       "slPSUSensorsVin": slPSUSensorsVin,
       "slPSUSensorsVout": slPSUSensorsVout,
       "slPSUSensorsIin": slPSUSensorsIin,
       "slPSUSensorsIout": slPSUSensorsIout,
       "slPSUSensorsPin": slPSUSensorsPin,
       "slPSUSensorsPout": slPSUSensorsPout}
)
