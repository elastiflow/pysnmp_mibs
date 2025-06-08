# SNMP MIB module (DIGI-PORTBUFFERING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-PORTBUFFERING-MIB.mib
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

(digiPortBuffering,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiPortBuffering")

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

_PortbufferTable_Object = MibTable
portbufferTable = _PortbufferTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 11, 11)
)
if mibBuilder.loadTexts:
    portbufferTable.setStatus("mandatory")
_PortbufferEntry_Object = MibTableRow
portbufferEntry = _PortbufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 11, 11, 1)
)
portbufferEntry.setIndexNames(
    (0, "DIGI-PORTBUFFERING-MIB", "portbufferIndex"),
)
if mibBuilder.loadTexts:
    portbufferEntry.setStatus("mandatory")
_PortbufferIndex_Type = Integer32
_PortbufferIndex_Object = MibTableColumn
portbufferIndex = _PortbufferIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 11, 11, 1, 11),
    _PortbufferIndex_Type()
)
portbufferIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portbufferIndex.setStatus("mandatory")


class _PortbufferState_Type(Integer32):
    """Custom type portbufferState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("paused", 3))
    )


_PortbufferState_Type.__name__ = "Integer32"
_PortbufferState_Object = MibTableColumn
portbufferState = _PortbufferState_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 11, 11, 1, 12),
    _PortbufferState_Type()
)
portbufferState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portbufferState.setStatus("mandatory")
_PortbufferSize_Type = Integer32
_PortbufferSize_Object = MibTableColumn
portbufferSize = _PortbufferSize_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 11, 11, 1, 13),
    _PortbufferSize_Type()
)
portbufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portbufferSize.setStatus("mandatory")
_PortbufferUsage_Type = Integer32
_PortbufferUsage_Object = MibTableColumn
portbufferUsage = _PortbufferUsage_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 11, 11, 1, 14),
    _PortbufferUsage_Type()
)
portbufferUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portbufferUsage.setStatus("mandatory")


class _PortbufferClear_Type(Integer32):
    """Custom type portbufferClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("clear", 2))
    )


_PortbufferClear_Type.__name__ = "Integer32"
_PortbufferClear_Object = MibTableColumn
portbufferClear = _PortbufferClear_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 11, 11, 1, 15),
    _PortbufferClear_Type()
)
portbufferClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portbufferClear.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-PORTBUFFERING-MIB",
    **{"portbufferTable": portbufferTable,
       "portbufferEntry": portbufferEntry,
       "portbufferIndex": portbufferIndex,
       "portbufferState": portbufferState,
       "portbufferSize": portbufferSize,
       "portbufferUsage": portbufferUsage,
       "portbufferClear": portbufferClear}
)
