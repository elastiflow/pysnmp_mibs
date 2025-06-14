# SNMP MIB module (BASIS-RAS-DISK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/stratacom_351/BASIS-RAS-DISK-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:03:53 2025
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

(axisDiagnostics,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "axisDiagnostics")

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

_RasDsk_ObjectIdentity = ObjectIdentity
rasDsk = _RasDsk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2)
)


class _RasDskStatus_Type(Integer32):
    """Custom type rasDskStatus based on Integer32"""
    defaultValue = 2

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


_RasDskStatus_Type.__name__ = "Integer32"
_RasDskStatus_Object = MibScalar
rasDskStatus = _RasDskStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 1),
    _RasDskStatus_Type()
)
rasDskStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rasDskStatus.setStatus("mandatory")


class _DskHealth_Type(Integer32):
    """Custom type dskHealth based on Integer32"""
    defaultValue = 3

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
        *(("pass", 1),
          ("fail", 2),
          ("unknown", 3),
          ("testInProgress", 4))
    )


_DskHealth_Type.__name__ = "Integer32"
_DskHealth_Object = MibScalar
dskHealth = _DskHealth_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 2),
    _DskHealth_Type()
)
dskHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskHealth.setStatus("mandatory")


class _StandbyDskHealth_Type(Integer32):
    """Custom type standbyDskHealth based on Integer32"""
    defaultValue = 3

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
        *(("pass", 1),
          ("fail", 2),
          ("unknown", 3),
          ("testInProgress", 4))
    )


_StandbyDskHealth_Type.__name__ = "Integer32"
_StandbyDskHealth_Object = MibScalar
standbyDskHealth = _StandbyDskHealth_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 3),
    _StandbyDskHealth_Type()
)
standbyDskHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standbyDskHealth.setStatus("mandatory")


class _WakeupInterval_Type(Integer32):
    """Custom type wakeupInterval based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12, 168),
    )


_WakeupInterval_Type.__name__ = "Integer32"
_WakeupInterval_Object = MibScalar
wakeupInterval = _WakeupInterval_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 4),
    _WakeupInterval_Type()
)
wakeupInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wakeupInterval.setStatus("mandatory")


class _LastTime_Type(DisplayString):
    """Custom type lastTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixedLength = 20


_LastTime_Type.__name__ = "DisplayString"
_LastTime_Object = MibScalar
lastTime = _LastTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 5),
    _LastTime_Type()
)
lastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastTime.setStatus("mandatory")


class _NumBadSectors_Type(Integer32):
    """Custom type numBadSectors based on Integer32"""
    defaultValue = 0


_NumBadSectors_Type.__name__ = "Integer32"
_NumBadSectors_Object = MibScalar
numBadSectors = _NumBadSectors_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 6),
    _NumBadSectors_Type()
)
numBadSectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBadSectors.setStatus("mandatory")


class _CrptdPRIfiles_Type(Integer32):
    """Custom type crptdPRIfiles based on Integer32"""
    defaultValue = 0


_CrptdPRIfiles_Type.__name__ = "Integer32"
_CrptdPRIfiles_Object = MibScalar
crptdPRIfiles = _CrptdPRIfiles_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 7),
    _CrptdPRIfiles_Type()
)
crptdPRIfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crptdPRIfiles.setStatus("mandatory")


class _CrptdFWfiles_Type(Integer32):
    """Custom type crptdFWfiles based on Integer32"""
    defaultValue = 0


_CrptdFWfiles_Type.__name__ = "Integer32"
_CrptdFWfiles_Object = MibScalar
crptdFWfiles = _CrptdFWfiles_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 8),
    _CrptdFWfiles_Type()
)
crptdFWfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crptdFWfiles.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BASIS-RAS-DISK-MIB",
    **{"rasDsk": rasDsk,
       "rasDskStatus": rasDskStatus,
       "dskHealth": dskHealth,
       "standbyDskHealth": standbyDskHealth,
       "wakeupInterval": wakeupInterval,
       "lastTime": lastTime,
       "numBadSectors": numBadSectors,
       "crptdPRIfiles": crptdPRIfiles,
       "crptdFWfiles": crptdFWfiles}
)
