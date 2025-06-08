# SNMP MIB module (GUDEADS-PDU818X-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gude_28507/GUDEADS-PDU818X-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:14:59 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

gudeads = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28507)
)
if mibBuilder.loadTexts:
    gudeads.setRevisions(
        ("2007-03-05 13:56",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GadsPDU818X_ObjectIdentity = ObjectIdentity
gadsPDU818X = _GadsPDU818X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 35)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 35, 0)
)
_Pdu818XObjects_ObjectIdentity = ObjectIdentity
pdu818XObjects = _Pdu818XObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1)
)
_Pdu818XCommonConfig_ObjectIdentity = ObjectIdentity
pdu818XCommonConfig = _Pdu818XCommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 1)
)
_Pdu818XSNMPaccess_ObjectIdentity = ObjectIdentity
pdu818XSNMPaccess = _Pdu818XSNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 1, 1)
)


class _Pdu818XTrapCtrl_Type(Integer32):
    """Custom type pdu818XTrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Pdu818XTrapCtrl_Type.__name__ = "Integer32"
_Pdu818XTrapCtrl_Object = MibScalar
pdu818XTrapCtrl = _Pdu818XTrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 1, 1, 1),
    _Pdu818XTrapCtrl_Type()
)
pdu818XTrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu818XTrapCtrl.setStatus("current")
_Pdu818XTrapIPTable_Object = MibTable
pdu818XTrapIPTable = _Pdu818XTrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pdu818XTrapIPTable.setStatus("current")
_Pdu818XTrapIPEntry_Object = MibTableRow
pdu818XTrapIPEntry = _Pdu818XTrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 1, 1, 2, 1)
)
pdu818XTrapIPEntry.setIndexNames(
    (0, "GUDEADS-PDU818X-MIB", "pdu818XTrapIPIndex"),
)
if mibBuilder.loadTexts:
    pdu818XTrapIPEntry.setStatus("current")


class _Pdu818XTrapIPIndex_Type(Integer32):
    """Custom type pdu818XTrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Pdu818XTrapIPIndex_Type.__name__ = "Integer32"
_Pdu818XTrapIPIndex_Object = MibTableColumn
pdu818XTrapIPIndex = _Pdu818XTrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 1, 1, 2, 1, 1),
    _Pdu818XTrapIPIndex_Type()
)
pdu818XTrapIPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdu818XTrapIPIndex.setStatus("current")


class _Pdu818XTrapAddr_Type(OctetString):
    """Custom type pdu818XTrapAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Pdu818XTrapAddr_Type.__name__ = "OctetString"
_Pdu818XTrapAddr_Object = MibTableColumn
pdu818XTrapAddr = _Pdu818XTrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 1, 1, 2, 1, 2),
    _Pdu818XTrapAddr_Type()
)
pdu818XTrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu818XTrapAddr.setStatus("current")
_Pdu818XDeviceConfig_ObjectIdentity = ObjectIdentity
pdu818XDeviceConfig = _Pdu818XDeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 2)
)
_Pdu818XIntActors_ObjectIdentity = ObjectIdentity
pdu818XIntActors = _Pdu818XIntActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 3)
)
_Pdu818XExtActors_ObjectIdentity = ObjectIdentity
pdu818XExtActors = _Pdu818XExtActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 4)
)
_Pdu818XIntSensors_ObjectIdentity = ObjectIdentity
pdu818XIntSensors = _Pdu818XIntSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 5)
)
_Pdu818XPowerChan_ObjectIdentity = ObjectIdentity
pdu818XPowerChan = _Pdu818XPowerChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 5, 1)
)


class _Pdu818XActivePowerChan_Type(Unsigned32):
    """Custom type pdu818XActivePowerChan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Pdu818XActivePowerChan_Type.__name__ = "Unsigned32"
_Pdu818XActivePowerChan_Object = MibScalar
pdu818XActivePowerChan = _Pdu818XActivePowerChan_Object(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 5, 1, 1),
    _Pdu818XActivePowerChan_Type()
)
pdu818XActivePowerChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu818XActivePowerChan.setStatus("current")
_Pdu818XPowerTable_Object = MibTable
pdu818XPowerTable = _Pdu818XPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    pdu818XPowerTable.setStatus("current")
_Pdu818XPowerEntry_Object = MibTableRow
pdu818XPowerEntry = _Pdu818XPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 5, 1, 2, 1)
)
pdu818XPowerEntry.setIndexNames(
    (0, "GUDEADS-PDU818X-MIB", "pdu818XPowerIndex"),
)
if mibBuilder.loadTexts:
    pdu818XPowerEntry.setStatus("current")


class _Pdu818XPowerIndex_Type(Integer32):
    """Custom type pdu818XPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Pdu818XPowerIndex_Type.__name__ = "Integer32"
_Pdu818XPowerIndex_Object = MibTableColumn
pdu818XPowerIndex = _Pdu818XPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 5, 1, 2, 1, 1),
    _Pdu818XPowerIndex_Type()
)
pdu818XPowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdu818XPowerIndex.setStatus("current")


class _Pdu818XChanStatus_Type(Integer32):
    """Custom type pdu818XChanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pdu818XChanStatus_Type.__name__ = "Integer32"
_Pdu818XChanStatus_Object = MibTableColumn
pdu818XChanStatus = _Pdu818XChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 5, 1, 2, 1, 2),
    _Pdu818XChanStatus_Type()
)
pdu818XChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu818XChanStatus.setStatus("current")
_Pdu818XEnergyActive_Type = Unsigned32
_Pdu818XEnergyActive_Object = MibTableColumn
pdu818XEnergyActive = _Pdu818XEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 5, 1, 2, 1, 3),
    _Pdu818XEnergyActive_Type()
)
pdu818XEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu818XEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    pdu818XEnergyActive.setUnits("Wh")
_Pdu818XPowerActive_Type = Unsigned32
_Pdu818XPowerActive_Object = MibTableColumn
pdu818XPowerActive = _Pdu818XPowerActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 5, 1, 2, 1, 4),
    _Pdu818XPowerActive_Type()
)
pdu818XPowerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu818XPowerActive.setStatus("current")
if mibBuilder.loadTexts:
    pdu818XPowerActive.setUnits("W")
_Pdu818XCurrent_Type = Unsigned32
_Pdu818XCurrent_Object = MibTableColumn
pdu818XCurrent = _Pdu818XCurrent_Object(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 5, 1, 2, 1, 5),
    _Pdu818XCurrent_Type()
)
pdu818XCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu818XCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pdu818XCurrent.setUnits("mA")
_Pdu818XVoltage_Type = Unsigned32
_Pdu818XVoltage_Object = MibTableColumn
pdu818XVoltage = _Pdu818XVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 5, 1, 2, 1, 6),
    _Pdu818XVoltage_Type()
)
pdu818XVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu818XVoltage.setStatus("current")
if mibBuilder.loadTexts:
    pdu818XVoltage.setUnits("V")
_Pdu818XExtSensors_ObjectIdentity = ObjectIdentity
pdu818XExtSensors = _Pdu818XExtSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 6)
)
_Pdu818XSensorTable_Object = MibTable
pdu818XSensorTable = _Pdu818XSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 6, 1)
)
if mibBuilder.loadTexts:
    pdu818XSensorTable.setStatus("current")
_Pdu818XSensorEntry_Object = MibTableRow
pdu818XSensorEntry = _Pdu818XSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 6, 1, 1)
)
pdu818XSensorEntry.setIndexNames(
    (0, "GUDEADS-PDU818X-MIB", "pdu818XSensorIndex"),
)
if mibBuilder.loadTexts:
    pdu818XSensorEntry.setStatus("current")


class _Pdu818XSensorIndex_Type(Integer32):
    """Custom type pdu818XSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Pdu818XSensorIndex_Type.__name__ = "Integer32"
_Pdu818XSensorIndex_Object = MibTableColumn
pdu818XSensorIndex = _Pdu818XSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 6, 1, 1, 1),
    _Pdu818XSensorIndex_Type()
)
pdu818XSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdu818XSensorIndex.setStatus("current")
_Pdu818XTempSensor_Type = Integer32
_Pdu818XTempSensor_Object = MibTableColumn
pdu818XTempSensor = _Pdu818XTempSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 6, 1, 1, 2),
    _Pdu818XTempSensor_Type()
)
pdu818XTempSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu818XTempSensor.setStatus("current")
if mibBuilder.loadTexts:
    pdu818XTempSensor.setUnits("10th of degree Celsius")
_Pdu818XHygroSensor_Type = Integer32
_Pdu818XHygroSensor_Object = MibTableColumn
pdu818XHygroSensor = _Pdu818XHygroSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 35, 1, 6, 1, 1, 3),
    _Pdu818XHygroSensor_Type()
)
pdu818XHygroSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu818XHygroSensor.setStatus("current")
if mibBuilder.loadTexts:
    pdu818XHygroSensor.setUnits("10th of percentage humidity")
_Pdu818XConf_ObjectIdentity = ObjectIdentity
pdu818XConf = _Pdu818XConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 35, 2)
)
_Pdu818XGroups_ObjectIdentity = ObjectIdentity
pdu818XGroups = _Pdu818XGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 35, 2, 1)
)
_Pdu818XCompls_ObjectIdentity = ObjectIdentity
pdu818XCompls = _Pdu818XCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 35, 2, 2)
)

# Managed Objects groups

pdu818XBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 35, 2, 1, 1)
)
pdu818XBasicGroup.setObjects(
      *(("GUDEADS-PDU818X-MIB", "pdu818XTrapCtrl"),
        ("GUDEADS-PDU818X-MIB", "pdu818XTrapAddr"),
        ("GUDEADS-PDU818X-MIB", "pdu818XTempSensor"),
        ("GUDEADS-PDU818X-MIB", "pdu818XHygroSensor"),
        ("GUDEADS-PDU818X-MIB", "pdu818XActivePowerChan"),
        ("GUDEADS-PDU818X-MIB", "pdu818XChanStatus"),
        ("GUDEADS-PDU818X-MIB", "pdu818XEnergyActive"),
        ("GUDEADS-PDU818X-MIB", "pdu818XPowerActive"),
        ("GUDEADS-PDU818X-MIB", "pdu818XCurrent"),
        ("GUDEADS-PDU818X-MIB", "pdu818XVoltage"))
)
if mibBuilder.loadTexts:
    pdu818XBasicGroup.setStatus("current")


# Notification objects

pdu818XPowerDataEvt1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 35, 0, 1)
)
pdu818XPowerDataEvt1.setObjects(
      *(("GUDEADS-PDU818X-MIB", "pdu818XEnergyActive"),
        ("GUDEADS-PDU818X-MIB", "pdu818XPowerActive"),
        ("GUDEADS-PDU818X-MIB", "pdu818XCurrent"),
        ("GUDEADS-PDU818X-MIB", "pdu818XVoltage"))
)
if mibBuilder.loadTexts:
    pdu818XPowerDataEvt1.setStatus(
        "current"
    )

pdu818XPowerDataEvt2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 35, 0, 2)
)
pdu818XPowerDataEvt2.setObjects(
      *(("GUDEADS-PDU818X-MIB", "pdu818XEnergyActive"),
        ("GUDEADS-PDU818X-MIB", "pdu818XPowerActive"),
        ("GUDEADS-PDU818X-MIB", "pdu818XCurrent"),
        ("GUDEADS-PDU818X-MIB", "pdu818XVoltage"))
)
if mibBuilder.loadTexts:
    pdu818XPowerDataEvt2.setStatus(
        "current"
    )

pdu818XPowerDataEvt3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 35, 0, 3)
)
pdu818XPowerDataEvt3.setObjects(
      *(("GUDEADS-PDU818X-MIB", "pdu818XEnergyActive"),
        ("GUDEADS-PDU818X-MIB", "pdu818XPowerActive"),
        ("GUDEADS-PDU818X-MIB", "pdu818XCurrent"),
        ("GUDEADS-PDU818X-MIB", "pdu818XVoltage"))
)
if mibBuilder.loadTexts:
    pdu818XPowerDataEvt3.setStatus(
        "current"
    )

pdu818XPowerDataEvt4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 35, 0, 4)
)
pdu818XPowerDataEvt4.setObjects(
      *(("GUDEADS-PDU818X-MIB", "pdu818XEnergyActive"),
        ("GUDEADS-PDU818X-MIB", "pdu818XPowerActive"),
        ("GUDEADS-PDU818X-MIB", "pdu818XCurrent"),
        ("GUDEADS-PDU818X-MIB", "pdu818XVoltage"))
)
if mibBuilder.loadTexts:
    pdu818XPowerDataEvt4.setStatus(
        "current"
    )

pdu818XTempEvtSen1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 35, 0, 6)
)
pdu818XTempEvtSen1.setObjects(
    ("GUDEADS-PDU818X-MIB", "pdu818XTempSensor")
)
if mibBuilder.loadTexts:
    pdu818XTempEvtSen1.setStatus(
        "current"
    )

pdu818XHygroEvtSen1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 35, 0, 7)
)
pdu818XHygroEvtSen1.setObjects(
    ("GUDEADS-PDU818X-MIB", "pdu818XHygroSensor")
)
if mibBuilder.loadTexts:
    pdu818XHygroEvtSen1.setStatus(
        "current"
    )


# Notifications groups

pdu818XNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 35, 2, 1, 2)
)
pdu818XNotificationGroup.setObjects(
      *(("GUDEADS-PDU818X-MIB", "pdu818XTempEvtSen1"),
        ("GUDEADS-PDU818X-MIB", "pdu818XHygroEvtSen1"),
        ("GUDEADS-PDU818X-MIB", "pdu818XPowerDataEvt1"),
        ("GUDEADS-PDU818X-MIB", "pdu818XPowerDataEvt2"),
        ("GUDEADS-PDU818X-MIB", "pdu818XPowerDataEvt3"),
        ("GUDEADS-PDU818X-MIB", "pdu818XPowerDataEvt4"))
)
if mibBuilder.loadTexts:
    pdu818XNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-PDU818X-MIB",
    **{"gudeads": gudeads,
       "gadsPDU818X": gadsPDU818X,
       "events": events,
       "pdu818XPowerDataEvt1": pdu818XPowerDataEvt1,
       "pdu818XPowerDataEvt2": pdu818XPowerDataEvt2,
       "pdu818XPowerDataEvt3": pdu818XPowerDataEvt3,
       "pdu818XPowerDataEvt4": pdu818XPowerDataEvt4,
       "pdu818XTempEvtSen1": pdu818XTempEvtSen1,
       "pdu818XHygroEvtSen1": pdu818XHygroEvtSen1,
       "pdu818XObjects": pdu818XObjects,
       "pdu818XCommonConfig": pdu818XCommonConfig,
       "pdu818XSNMPaccess": pdu818XSNMPaccess,
       "pdu818XTrapCtrl": pdu818XTrapCtrl,
       "pdu818XTrapIPTable": pdu818XTrapIPTable,
       "pdu818XTrapIPEntry": pdu818XTrapIPEntry,
       "pdu818XTrapIPIndex": pdu818XTrapIPIndex,
       "pdu818XTrapAddr": pdu818XTrapAddr,
       "pdu818XDeviceConfig": pdu818XDeviceConfig,
       "pdu818XIntActors": pdu818XIntActors,
       "pdu818XExtActors": pdu818XExtActors,
       "pdu818XIntSensors": pdu818XIntSensors,
       "pdu818XPowerChan": pdu818XPowerChan,
       "pdu818XActivePowerChan": pdu818XActivePowerChan,
       "pdu818XPowerTable": pdu818XPowerTable,
       "pdu818XPowerEntry": pdu818XPowerEntry,
       "pdu818XPowerIndex": pdu818XPowerIndex,
       "pdu818XChanStatus": pdu818XChanStatus,
       "pdu818XEnergyActive": pdu818XEnergyActive,
       "pdu818XPowerActive": pdu818XPowerActive,
       "pdu818XCurrent": pdu818XCurrent,
       "pdu818XVoltage": pdu818XVoltage,
       "pdu818XExtSensors": pdu818XExtSensors,
       "pdu818XSensorTable": pdu818XSensorTable,
       "pdu818XSensorEntry": pdu818XSensorEntry,
       "pdu818XSensorIndex": pdu818XSensorIndex,
       "pdu818XTempSensor": pdu818XTempSensor,
       "pdu818XHygroSensor": pdu818XHygroSensor,
       "pdu818XConf": pdu818XConf,
       "pdu818XGroups": pdu818XGroups,
       "pdu818XBasicGroup": pdu818XBasicGroup,
       "pdu818XNotificationGroup": pdu818XNotificationGroup,
       "pdu818XCompls": pdu818XCompls}
)
