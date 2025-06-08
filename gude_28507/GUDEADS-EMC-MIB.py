# SNMP MIB module (GUDEADS-EMC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gude_28507/GUDEADS-EMC-MIB.mib
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
        ("2007-05-23 12:44",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GadsEMC_ObjectIdentity = ObjectIdentity
gadsEMC = _GadsEMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 3)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 3, 0)
)
_GadsObjects_ObjectIdentity = ObjectIdentity
gadsObjects = _GadsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 3, 1)
)
_EmcSNMPaccess_ObjectIdentity = ObjectIdentity
emcSNMPaccess = _EmcSNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 3, 1, 1)
)


class _EmcTrapCtrl_Type(Integer32):
    """Custom type emcTrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_EmcTrapCtrl_Type.__name__ = "Integer32"
_EmcTrapCtrl_Object = MibScalar
emcTrapCtrl = _EmcTrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 3, 1, 1, 1),
    _EmcTrapCtrl_Type()
)
emcTrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emcTrapCtrl.setStatus("current")
_EmcTrapIPTable_Object = MibTable
emcTrapIPTable = _EmcTrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    emcTrapIPTable.setStatus("current")
_EmcTrapIPEntry_Object = MibTableRow
emcTrapIPEntry = _EmcTrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 3, 1, 1, 2, 1)
)
emcTrapIPEntry.setIndexNames(
    (0, "GUDEADS-EMC-MIB", "emcTrapIPIndex"),
)
if mibBuilder.loadTexts:
    emcTrapIPEntry.setStatus("current")


class _EmcTrapIPIndex_Type(Integer32):
    """Custom type emcTrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_EmcTrapIPIndex_Type.__name__ = "Integer32"
_EmcTrapIPIndex_Object = MibTableColumn
emcTrapIPIndex = _EmcTrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 3, 1, 1, 2, 1, 1),
    _EmcTrapIPIndex_Type()
)
emcTrapIPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    emcTrapIPIndex.setStatus("current")


class _EmcTrapIPAddr_Type(IpAddress):
    """Custom type emcTrapIPAddr based on IpAddress"""
    defaultHexValue = "00000000"


_EmcTrapIPAddr_Type.__name__ = "IpAddress"
_EmcTrapIPAddr_Object = MibTableColumn
emcTrapIPAddr = _EmcTrapIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 3, 1, 1, 2, 1, 2),
    _EmcTrapIPAddr_Type()
)
emcTrapIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emcTrapIPAddr.setStatus("current")


class _EmcTrapIPPort_Type(Integer32):
    """Custom type emcTrapIPPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_EmcTrapIPPort_Type.__name__ = "Integer32"
_EmcTrapIPPort_Object = MibTableColumn
emcTrapIPPort = _EmcTrapIPPort_Object(
    (1, 3, 6, 1, 4, 1, 28507, 3, 1, 1, 2, 1, 3),
    _EmcTrapIPPort_Type()
)
emcTrapIPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emcTrapIPPort.setStatus("current")
_EmcTime_Type = Unsigned32
_EmcTime_Object = MibScalar
emcTime = _EmcTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 3, 1, 2),
    _EmcTime_Type()
)
emcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcTime.setStatus("current")
if mibBuilder.loadTexts:
    emcTime.setUnits("seconds")
_EmcTimeFrac_Type = Unsigned32
_EmcTimeFrac_Object = MibScalar
emcTimeFrac = _EmcTimeFrac_Object(
    (1, 3, 6, 1, 4, 1, 28507, 3, 1, 3),
    _EmcTimeFrac_Type()
)
emcTimeFrac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcTimeFrac.setStatus("current")
if mibBuilder.loadTexts:
    emcTimeFrac.setUnits("miliseconds")


class _EmcRelaisState_Type(Integer32):
    """Custom type emcRelaisState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EmcRelaisState_Type.__name__ = "Integer32"
_EmcRelaisState_Object = MibScalar
emcRelaisState = _EmcRelaisState_Object(
    (1, 3, 6, 1, 4, 1, 28507, 3, 1, 4),
    _EmcRelaisState_Type()
)
emcRelaisState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emcRelaisState.setStatus("current")
if mibBuilder.loadTexts:
    emcRelaisState.setUnits("Bool")


class _EmcDCF77mode_Type(Integer32):
    """Custom type emcDCF77mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("quartz", 0),
          ("dcf77", 1))
    )


_EmcDCF77mode_Type.__name__ = "Integer32"
_EmcDCF77mode_Object = MibScalar
emcDCF77mode = _EmcDCF77mode_Object(
    (1, 3, 6, 1, 4, 1, 28507, 3, 1, 5),
    _EmcDCF77mode_Type()
)
emcDCF77mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcDCF77mode.setStatus("current")
if mibBuilder.loadTexts:
    emcDCF77mode.setUnits("Bool")
_EmcTemperature_Type = Integer32
_EmcTemperature_Object = MibScalar
emcTemperature = _EmcTemperature_Object(
    (1, 3, 6, 1, 4, 1, 28507, 3, 1, 6),
    _EmcTemperature_Type()
)
emcTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emcTemperature.setStatus("current")
if mibBuilder.loadTexts:
    emcTemperature.setUnits("10th of degree Celsius")
_EmcEvents_ObjectIdentity = ObjectIdentity
emcEvents = _EmcEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 3, 2)
)
_EmcConf_ObjectIdentity = ObjectIdentity
emcConf = _EmcConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 3, 3)
)
_EmcGroups_ObjectIdentity = ObjectIdentity
emcGroups = _EmcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 3, 3, 1)
)
_EmcCompls_ObjectIdentity = ObjectIdentity
emcCompls = _EmcCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 3, 3, 2)
)

# Managed Objects groups

emcBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 3, 3, 1, 1)
)
emcBasicGroup.setObjects(
      *(("GUDEADS-EMC-MIB", "emcTime"),
        ("GUDEADS-EMC-MIB", "emcTimeFrac"),
        ("GUDEADS-EMC-MIB", "emcRelaisState"),
        ("GUDEADS-EMC-MIB", "emcTrapCtrl"),
        ("GUDEADS-EMC-MIB", "emcTrapIPAddr"),
        ("GUDEADS-EMC-MIB", "emcTrapIPPort"),
        ("GUDEADS-EMC-MIB", "emcDCF77mode"),
        ("GUDEADS-EMC-MIB", "emcTemperature"))
)
if mibBuilder.loadTexts:
    emcBasicGroup.setStatus("current")


# Notification objects

emcTempEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 3, 0, 1)
)
emcTempEvt.setObjects(
    ("GUDEADS-EMC-MIB", "emcTemperature")
)
if mibBuilder.loadTexts:
    emcTempEvt.setStatus(
        "current"
    )

emcRelaisEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 3, 0, 2)
)
emcRelaisEvt.setObjects(
    ("GUDEADS-EMC-MIB", "emcRelaisState")
)
if mibBuilder.loadTexts:
    emcRelaisEvt.setStatus(
        "current"
    )

emcDCF77Evt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 3, 0, 3)
)
emcDCF77Evt.setObjects(
    ("GUDEADS-EMC-MIB", "emcDCF77mode")
)
if mibBuilder.loadTexts:
    emcDCF77Evt.setStatus(
        "current"
    )


# Notifications groups

emcNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 3, 3, 1, 2)
)
emcNotificationGroup.setObjects(
      *(("GUDEADS-EMC-MIB", "emcTempEvt"),
        ("GUDEADS-EMC-MIB", "emcRelaisEvt"),
        ("GUDEADS-EMC-MIB", "emcDCF77Evt"))
)
if mibBuilder.loadTexts:
    emcNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-EMC-MIB",
    **{"gudeads": gudeads,
       "gadsEMC": gadsEMC,
       "events": events,
       "emcTempEvt": emcTempEvt,
       "emcRelaisEvt": emcRelaisEvt,
       "emcDCF77Evt": emcDCF77Evt,
       "gadsObjects": gadsObjects,
       "emcSNMPaccess": emcSNMPaccess,
       "emcTrapCtrl": emcTrapCtrl,
       "emcTrapIPTable": emcTrapIPTable,
       "emcTrapIPEntry": emcTrapIPEntry,
       "emcTrapIPIndex": emcTrapIPIndex,
       "emcTrapIPAddr": emcTrapIPAddr,
       "emcTrapIPPort": emcTrapIPPort,
       "emcTime": emcTime,
       "emcTimeFrac": emcTimeFrac,
       "emcRelaisState": emcRelaisState,
       "emcDCF77mode": emcDCF77mode,
       "emcTemperature": emcTemperature,
       "emcEvents": emcEvents,
       "emcConf": emcConf,
       "emcGroups": emcGroups,
       "emcBasicGroup": emcBasicGroup,
       "emcNotificationGroup": emcNotificationGroup,
       "emcCompls": emcCompls}
)
