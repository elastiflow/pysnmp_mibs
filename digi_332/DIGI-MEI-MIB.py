# SNMP MIB module (DIGI-MEI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-MEI-MIB.mib
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

(digiMei,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiMei")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MeiTable_Object = MibTable
meiTable = _MeiTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 11, 11)
)
if mibBuilder.loadTexts:
    meiTable.setStatus("mandatory")
_MeiEntry_Object = MibTableRow
meiEntry = _MeiEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 11, 11, 1)
)
meiEntry.setIndexNames(
    (0, "DIGI-MEI-MIB", "meiIndex"),
)
if mibBuilder.loadTexts:
    meiEntry.setStatus("mandatory")
_MeiIndex_Type = Integer32
_MeiIndex_Object = MibTableColumn
meiIndex = _MeiIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 11, 11, 1, 11),
    _MeiIndex_Type()
)
meiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meiIndex.setStatus("mandatory")
_MeiDescription_Type = DisplayString
_MeiDescription_Object = MibTableColumn
meiDescription = _MeiDescription_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 11, 11, 1, 12),
    _MeiDescription_Type()
)
meiDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meiDescription.setStatus("mandatory")


class _MeiPortType_Type(Integer32):
    """Custom type meiPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("rs232", 2),
          ("rs422-rs485", 3))
    )


_MeiPortType_Type.__name__ = "Integer32"
_MeiPortType_Object = MibTableColumn
meiPortType = _MeiPortType_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 11, 11, 1, 13),
    _MeiPortType_Type()
)
meiPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meiPortType.setStatus("mandatory")


class _MeiMode_Type(Integer32):
    """Custom type meiMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("two-wire", 2),
          ("four-wire", 3))
    )


_MeiMode_Type.__name__ = "Integer32"
_MeiMode_Object = MibTableColumn
meiMode = _MeiMode_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 11, 11, 1, 14),
    _MeiMode_Type()
)
meiMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meiMode.setStatus("mandatory")


class _MeiDuplex_Type(Integer32):
    """Custom type meiDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("half", 2),
          ("full", 3))
    )


_MeiDuplex_Type.__name__ = "Integer32"
_MeiDuplex_Object = MibTableColumn
meiDuplex = _MeiDuplex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 11, 11, 1, 15),
    _MeiDuplex_Type()
)
meiDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meiDuplex.setStatus("mandatory")


class _MeiTermination_Type(Integer32):
    """Custom type meiTermination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("un-terminated", 2),
          ("terminated", 3))
    )


_MeiTermination_Type.__name__ = "Integer32"
_MeiTermination_Object = MibTableColumn
meiTermination = _MeiTermination_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 11, 11, 1, 16),
    _MeiTermination_Type()
)
meiTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meiTermination.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-MEI-MIB",
    **{"DisplayString": DisplayString,
       "meiTable": meiTable,
       "meiEntry": meiEntry,
       "meiIndex": meiIndex,
       "meiDescription": meiDescription,
       "meiPortType": meiPortType,
       "meiMode": meiMode,
       "meiDuplex": meiDuplex,
       "meiTermination": meiTermination}
)
