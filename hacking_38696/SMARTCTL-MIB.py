# SNMP MIB module (SMARTCTL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/hacking_38696/SMARTCTL-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:21:09 2025
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

(hackingExperimental,) = mibBuilder.importSymbols(
    "HACKING-SNMP-MIB",
    "hackingExperimental")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

smartCtlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 38696, 2, 1, 1)
)
if mibBuilder.loadTexts:
    smartCtlMIB.setRevisions(
        ("2011-09-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SmartCtl_ObjectIdentity = ObjectIdentity
smartCtl = _SmartCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38696, 2, 1)
)
_SmartCtlTable_Object = MibTable
smartCtlTable = _SmartCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 1, 2)
)
if mibBuilder.loadTexts:
    smartCtlTable.setStatus("current")
_SmartCtlEntry_Object = MibTableRow
smartCtlEntry = _SmartCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 1, 2, 1)
)
smartCtlEntry.setIndexNames(
    (0, "SMARTCTL-MIB", "smartCtlDeviceIndex"),
)
if mibBuilder.loadTexts:
    smartCtlEntry.setStatus("current")


class _SmartCtlDeviceIndex_Type(Integer32):
    """Custom type smartCtlDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SmartCtlDeviceIndex_Type.__name__ = "Integer32"
_SmartCtlDeviceIndex_Object = MibTableColumn
smartCtlDeviceIndex = _SmartCtlDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 1, 2, 1, 1),
    _SmartCtlDeviceIndex_Type()
)
smartCtlDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartCtlDeviceIndex.setStatus("current")
_SmartCtlDeviceDev_Type = DisplayString
_SmartCtlDeviceDev_Object = MibTableColumn
smartCtlDeviceDev = _SmartCtlDeviceDev_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 1, 2, 1, 2),
    _SmartCtlDeviceDev_Type()
)
smartCtlDeviceDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartCtlDeviceDev.setStatus("current")
_SmartCtlDeviceModelFamily_Type = DisplayString
_SmartCtlDeviceModelFamily_Object = MibTableColumn
smartCtlDeviceModelFamily = _SmartCtlDeviceModelFamily_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 1, 2, 1, 3),
    _SmartCtlDeviceModelFamily_Type()
)
smartCtlDeviceModelFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartCtlDeviceModelFamily.setStatus("current")
_SmartCtlDeviceDeviceModel_Type = DisplayString
_SmartCtlDeviceDeviceModel_Object = MibTableColumn
smartCtlDeviceDeviceModel = _SmartCtlDeviceDeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 1, 2, 1, 4),
    _SmartCtlDeviceDeviceModel_Type()
)
smartCtlDeviceDeviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartCtlDeviceDeviceModel.setStatus("current")
_SmartCtlDeviceSerialNumber_Type = DisplayString
_SmartCtlDeviceSerialNumber_Object = MibTableColumn
smartCtlDeviceSerialNumber = _SmartCtlDeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 1, 2, 1, 5),
    _SmartCtlDeviceSerialNumber_Type()
)
smartCtlDeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartCtlDeviceSerialNumber.setStatus("current")
_SmartCtlDeviceUserCapacity_Type = DisplayString
_SmartCtlDeviceUserCapacity_Object = MibTableColumn
smartCtlDeviceUserCapacity = _SmartCtlDeviceUserCapacity_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 1, 2, 1, 6),
    _SmartCtlDeviceUserCapacity_Type()
)
smartCtlDeviceUserCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartCtlDeviceUserCapacity.setStatus("current")
_SmartCtlDeviceATAVersion_Type = DisplayString
_SmartCtlDeviceATAVersion_Object = MibTableColumn
smartCtlDeviceATAVersion = _SmartCtlDeviceATAVersion_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 1, 2, 1, 7),
    _SmartCtlDeviceATAVersion_Type()
)
smartCtlDeviceATAVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartCtlDeviceATAVersion.setStatus("current")
_SmartCtlDeviceHealthOK_Type = TruthValue
_SmartCtlDeviceHealthOK_Object = MibTableColumn
smartCtlDeviceHealthOK = _SmartCtlDeviceHealthOK_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 1, 2, 1, 8),
    _SmartCtlDeviceHealthOK_Type()
)
smartCtlDeviceHealthOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartCtlDeviceHealthOK.setStatus("current")
_SmartCtlDeviceTemperatureCelsius_Type = Gauge32
_SmartCtlDeviceTemperatureCelsius_Object = MibTableColumn
smartCtlDeviceTemperatureCelsius = _SmartCtlDeviceTemperatureCelsius_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 1, 2, 1, 9),
    _SmartCtlDeviceTemperatureCelsius_Type()
)
smartCtlDeviceTemperatureCelsius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartCtlDeviceTemperatureCelsius.setStatus("current")
_SmartCtlDeviceReallocatedSectorCt_Type = Gauge32
_SmartCtlDeviceReallocatedSectorCt_Object = MibTableColumn
smartCtlDeviceReallocatedSectorCt = _SmartCtlDeviceReallocatedSectorCt_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 1, 2, 1, 10),
    _SmartCtlDeviceReallocatedSectorCt_Type()
)
smartCtlDeviceReallocatedSectorCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartCtlDeviceReallocatedSectorCt.setStatus("current")
_SmartCtlDeviceCurrentPendingSector_Type = Gauge32
_SmartCtlDeviceCurrentPendingSector_Object = MibTableColumn
smartCtlDeviceCurrentPendingSector = _SmartCtlDeviceCurrentPendingSector_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 1, 2, 1, 11),
    _SmartCtlDeviceCurrentPendingSector_Type()
)
smartCtlDeviceCurrentPendingSector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartCtlDeviceCurrentPendingSector.setStatus("current")
_SmartCtlDeviceOfflineUncorrectable_Type = Gauge32
_SmartCtlDeviceOfflineUncorrectable_Object = MibTableColumn
smartCtlDeviceOfflineUncorrectable = _SmartCtlDeviceOfflineUncorrectable_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 1, 2, 1, 12),
    _SmartCtlDeviceOfflineUncorrectable_Type()
)
smartCtlDeviceOfflineUncorrectable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartCtlDeviceOfflineUncorrectable.setStatus("current")
_SmartCtlDeviceUDMACRCErrorCount_Type = Gauge32
_SmartCtlDeviceUDMACRCErrorCount_Object = MibTableColumn
smartCtlDeviceUDMACRCErrorCount = _SmartCtlDeviceUDMACRCErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 1, 2, 1, 13),
    _SmartCtlDeviceUDMACRCErrorCount_Type()
)
smartCtlDeviceUDMACRCErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartCtlDeviceUDMACRCErrorCount.setStatus("current")
_SmartCtlDeviceReadErrorRate_Type = Gauge32
_SmartCtlDeviceReadErrorRate_Object = MibTableColumn
smartCtlDeviceReadErrorRate = _SmartCtlDeviceReadErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 1, 2, 1, 14),
    _SmartCtlDeviceReadErrorRate_Type()
)
smartCtlDeviceReadErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartCtlDeviceReadErrorRate.setStatus("current")
_SmartCtlDeviceSeekErrorRate_Type = Gauge32
_SmartCtlDeviceSeekErrorRate_Object = MibTableColumn
smartCtlDeviceSeekErrorRate = _SmartCtlDeviceSeekErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 1, 2, 1, 15),
    _SmartCtlDeviceSeekErrorRate_Type()
)
smartCtlDeviceSeekErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartCtlDeviceSeekErrorRate.setStatus("current")
_SmartCtlDeviceHardwareECCRecovered_Type = Gauge32
_SmartCtlDeviceHardwareECCRecovered_Object = MibTableColumn
smartCtlDeviceHardwareECCRecovered = _SmartCtlDeviceHardwareECCRecovered_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 1, 2, 1, 16),
    _SmartCtlDeviceHardwareECCRecovered_Type()
)
smartCtlDeviceHardwareECCRecovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartCtlDeviceHardwareECCRecovered.setStatus("current")
_SmartCtlDeviceFirmwareVersion_Type = DisplayString
_SmartCtlDeviceFirmwareVersion_Object = MibTableColumn
smartCtlDeviceFirmwareVersion = _SmartCtlDeviceFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 1, 2, 1, 17),
    _SmartCtlDeviceFirmwareVersion_Type()
)
smartCtlDeviceFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartCtlDeviceFirmwareVersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SMARTCTL-MIB",
    **{"smartCtl": smartCtl,
       "smartCtlMIB": smartCtlMIB,
       "smartCtlTable": smartCtlTable,
       "smartCtlEntry": smartCtlEntry,
       "smartCtlDeviceIndex": smartCtlDeviceIndex,
       "smartCtlDeviceDev": smartCtlDeviceDev,
       "smartCtlDeviceModelFamily": smartCtlDeviceModelFamily,
       "smartCtlDeviceDeviceModel": smartCtlDeviceDeviceModel,
       "smartCtlDeviceSerialNumber": smartCtlDeviceSerialNumber,
       "smartCtlDeviceUserCapacity": smartCtlDeviceUserCapacity,
       "smartCtlDeviceATAVersion": smartCtlDeviceATAVersion,
       "smartCtlDeviceHealthOK": smartCtlDeviceHealthOK,
       "smartCtlDeviceTemperatureCelsius": smartCtlDeviceTemperatureCelsius,
       "smartCtlDeviceReallocatedSectorCt": smartCtlDeviceReallocatedSectorCt,
       "smartCtlDeviceCurrentPendingSector": smartCtlDeviceCurrentPendingSector,
       "smartCtlDeviceOfflineUncorrectable": smartCtlDeviceOfflineUncorrectable,
       "smartCtlDeviceUDMACRCErrorCount": smartCtlDeviceUDMACRCErrorCount,
       "smartCtlDeviceReadErrorRate": smartCtlDeviceReadErrorRate,
       "smartCtlDeviceSeekErrorRate": smartCtlDeviceSeekErrorRate,
       "smartCtlDeviceHardwareECCRecovered": smartCtlDeviceHardwareECCRecovered,
       "smartCtlDeviceFirmwareVersion": smartCtlDeviceFirmwareVersion}
)
