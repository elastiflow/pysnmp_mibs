# SNMP MIB module (CONEL-STATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/advantech_30140/CONEL-STATUS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:15:06 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Conel_ObjectIdentity = ObjectIdentity
conel = _Conel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140)
)
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 3)
)


class _StatusMBusOverload1_Type(Integer32):
    """Custom type statusMBusOverload1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_StatusMBusOverload1_Type.__name__ = "Integer32"
_StatusMBusOverload1_Object = MibScalar
statusMBusOverload1 = _StatusMBusOverload1_Object(
    (1, 3, 6, 1, 4, 1, 30140, 3, 1),
    _StatusMBusOverload1_Type()
)
statusMBusOverload1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusMBusOverload1.setStatus("mandatory")


class _StatusMBusOverload2_Type(Integer32):
    """Custom type statusMBusOverload2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_StatusMBusOverload2_Type.__name__ = "Integer32"
_StatusMBusOverload2_Object = MibScalar
statusMBusOverload2 = _StatusMBusOverload2_Object(
    (1, 3, 6, 1, 4, 1, 30140, 3, 2),
    _StatusMBusOverload2_Type()
)
statusMBusOverload2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusMBusOverload2.setStatus("mandatory")
_StatusTemperature_Type = Integer32
_StatusTemperature_Object = MibScalar
statusTemperature = _StatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 30140, 3, 3),
    _StatusTemperature_Type()
)
statusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusTemperature.setStatus("mandatory")
_StatusVoltage_Type = Integer32
_StatusVoltage_Object = MibScalar
statusVoltage = _StatusVoltage_Object(
    (1, 3, 6, 1, 4, 1, 30140, 3, 4),
    _StatusVoltage_Type()
)
statusVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusVoltage.setStatus("mandatory")


class _StatusRTCBattery_Type(Integer32):
    """Custom type statusRTCBattery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ok", 1),
          ("empty", 2))
    )


_StatusRTCBattery_Type.__name__ = "Integer32"
_StatusRTCBattery_Object = MibScalar
statusRTCBattery = _StatusRTCBattery_Object(
    (1, 3, 6, 1, 4, 1, 30140, 3, 5),
    _StatusRTCBattery_Type()
)
statusRTCBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRTCBattery.setStatus("mandatory")
_StatusCPUUsage_Type = Gauge32
_StatusCPUUsage_Object = MibScalar
statusCPUUsage = _StatusCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 30140, 3, 6),
    _StatusCPUUsage_Type()
)
statusCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusCPUUsage.setStatus("mandatory")
_StatusRAMUsage_Type = Gauge32
_StatusRAMUsage_Object = MibScalar
statusRAMUsage = _StatusRAMUsage_Object(
    (1, 3, 6, 1, 4, 1, 30140, 3, 7),
    _StatusRAMUsage_Type()
)
statusRAMUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRAMUsage.setStatus("mandatory")
_StatusRAMUsed_Type = Gauge32
_StatusRAMUsed_Object = MibScalar
statusRAMUsed = _StatusRAMUsed_Object(
    (1, 3, 6, 1, 4, 1, 30140, 3, 8),
    _StatusRAMUsed_Type()
)
statusRAMUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRAMUsed.setStatus("mandatory")
_StatusRAMFree_Type = Gauge32
_StatusRAMFree_Object = MibScalar
statusRAMFree = _StatusRAMFree_Object(
    (1, 3, 6, 1, 4, 1, 30140, 3, 9),
    _StatusRAMFree_Type()
)
statusRAMFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRAMFree.setStatus("mandatory")
_StatusRAMTotal_Type = Gauge32
_StatusRAMTotal_Object = MibScalar
statusRAMTotal = _StatusRAMTotal_Object(
    (1, 3, 6, 1, 4, 1, 30140, 3, 10),
    _StatusRAMTotal_Type()
)
statusRAMTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRAMTotal.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONEL-STATUS-MIB",
    **{"conel": conel,
       "status": status,
       "statusMBusOverload1": statusMBusOverload1,
       "statusMBusOverload2": statusMBusOverload2,
       "statusTemperature": statusTemperature,
       "statusVoltage": statusVoltage,
       "statusRTCBattery": statusRTCBattery,
       "statusCPUUsage": statusCPUUsage,
       "statusRAMUsage": statusRAMUsage,
       "statusRAMUsed": statusRAMUsed,
       "statusRAMFree": statusRAMFree,
       "statusRAMTotal": statusRAMTotal}
)
