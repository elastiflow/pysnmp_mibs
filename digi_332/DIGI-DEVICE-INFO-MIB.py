# SNMP MIB module (DIGI-DEVICE-INFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-DEVICE-INFO-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:54:30 2025
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

(digiDeviceInfo,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiDeviceInfo")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DiProduct_Type = OctetString
_DiProduct_Object = MibScalar
diProduct = _DiProduct_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 1, 1),
    _DiProduct_Type()
)
diProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diProduct.setStatus("mandatory")
_DiPhysicalAddress_Type = OctetString
_DiPhysicalAddress_Object = MibScalar
diPhysicalAddress = _DiPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 1, 2),
    _DiPhysicalAddress_Type()
)
diPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diPhysicalAddress.setStatus("mandatory")
_DiFirmwareVersion_Type = OctetString
_DiFirmwareVersion_Object = MibScalar
diFirmwareVersion = _DiFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 1, 3),
    _DiFirmwareVersion_Type()
)
diFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diFirmwareVersion.setStatus("mandatory")
_DiBootVersion_Type = OctetString
_DiBootVersion_Object = MibScalar
diBootVersion = _DiBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 1, 4),
    _DiBootVersion_Type()
)
diBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diBootVersion.setStatus("mandatory")
_DiPostVersion_Type = OctetString
_DiPostVersion_Object = MibScalar
diPostVersion = _DiPostVersion_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 1, 5),
    _DiPostVersion_Type()
)
diPostVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diPostVersion.setStatus("mandatory")


class _DiCpuUtilization_Type(Integer32):
    """Custom type diCpuUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DiCpuUtilization_Type.__name__ = "Integer32"
_DiCpuUtilization_Object = MibScalar
diCpuUtilization = _DiCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 1, 6),
    _DiCpuUtilization_Type()
)
diCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diCpuUtilization.setStatus("mandatory")
_DiUpTime_Type = OctetString
_DiUpTime_Object = MibScalar
diUpTime = _DiUpTime_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 1, 7),
    _DiUpTime_Type()
)
diUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diUpTime.setStatus("mandatory")
_DiTotalMemory_Type = Integer32
_DiTotalMemory_Object = MibScalar
diTotalMemory = _DiTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 1, 8),
    _DiTotalMemory_Type()
)
diTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diTotalMemory.setStatus("mandatory")
_DiFreeMemory_Type = Integer32
_DiFreeMemory_Object = MibScalar
diFreeMemory = _DiFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 1, 9),
    _DiFreeMemory_Type()
)
diFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diFreeMemory.setStatus("mandatory")
_DiUsedMemory_Type = Integer32
_DiUsedMemory_Object = MibScalar
diUsedMemory = _DiUsedMemory_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 1, 10),
    _DiUsedMemory_Type()
)
diUsedMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diUsedMemory.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-DEVICE-INFO-MIB",
    **{"diProduct": diProduct,
       "diPhysicalAddress": diPhysicalAddress,
       "diFirmwareVersion": diFirmwareVersion,
       "diBootVersion": diBootVersion,
       "diPostVersion": diPostVersion,
       "diCpuUtilization": diCpuUtilization,
       "diUpTime": diUpTime,
       "diTotalMemory": diTotalMemory,
       "diFreeMemory": diFreeMemory,
       "diUsedMemory": diUsedMemory}
)
