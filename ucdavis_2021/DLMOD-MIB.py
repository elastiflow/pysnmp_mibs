# SNMP MIB module (DLMOD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ucdavis_2021/DLMOD-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 19:49:14 2025
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

(ucdavis,) = mibBuilder.importSymbols(
    "UCD-SNMP-MIB",
    "ucdavis")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dlmod_ObjectIdentity = ObjectIdentity
dlmod = _Dlmod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 14)
)
_DlmodNextIndex_Type = Integer32
_DlmodNextIndex_Object = MibScalar
dlmodNextIndex = _DlmodNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 14, 1),
    _DlmodNextIndex_Type()
)
dlmodNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlmodNextIndex.setStatus("current")
_DlmodTable_Object = MibTable
dlmodTable = _DlmodTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 14, 2)
)
if mibBuilder.loadTexts:
    dlmodTable.setStatus("current")
_DlmodEntry_Object = MibTableRow
dlmodEntry = _DlmodEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 14, 2, 1)
)
dlmodEntry.setIndexNames(
    (0, "DLMOD-MIB", "dlmodIndex"),
)
if mibBuilder.loadTexts:
    dlmodEntry.setStatus("current")


class _DlmodIndex_Type(Integer32):
    """Custom type dlmodIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DlmodIndex_Type.__name__ = "Integer32"
_DlmodIndex_Object = MibTableColumn
dlmodIndex = _DlmodIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 14, 2, 1, 1),
    _DlmodIndex_Type()
)
dlmodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlmodIndex.setStatus("current")


class _DlmodName_Type(DisplayString):
    """Custom type dlmodName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DlmodName_Type.__name__ = "DisplayString"
_DlmodName_Object = MibTableColumn
dlmodName = _DlmodName_Object(
    (1, 3, 6, 1, 4, 1, 2021, 14, 2, 1, 2),
    _DlmodName_Type()
)
dlmodName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlmodName.setStatus("current")


class _DlmodPath_Type(DisplayString):
    """Custom type dlmodPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DlmodPath_Type.__name__ = "DisplayString"
_DlmodPath_Object = MibTableColumn
dlmodPath = _DlmodPath_Object(
    (1, 3, 6, 1, 4, 1, 2021, 14, 2, 1, 3),
    _DlmodPath_Type()
)
dlmodPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlmodPath.setStatus("current")


class _DlmodError_Type(DisplayString):
    """Custom type dlmodError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DlmodError_Type.__name__ = "DisplayString"
_DlmodError_Object = MibTableColumn
dlmodError = _DlmodError_Object(
    (1, 3, 6, 1, 4, 1, 2021, 14, 2, 1, 4),
    _DlmodError_Type()
)
dlmodError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlmodError.setStatus("current")


class _DlmodStatus_Type(Integer32):
    """Custom type dlmodStatus based on Integer32"""
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
        *(("loaded", 1),
          ("unloaded", 2),
          ("error", 3),
          ("load", 4),
          ("unload", 5),
          ("create", 6),
          ("delete", 7))
    )


_DlmodStatus_Type.__name__ = "Integer32"
_DlmodStatus_Object = MibTableColumn
dlmodStatus = _DlmodStatus_Object(
    (1, 3, 6, 1, 4, 1, 2021, 14, 2, 1, 5),
    _DlmodStatus_Type()
)
dlmodStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlmodStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLMOD-MIB",
    **{"dlmod": dlmod,
       "dlmodNextIndex": dlmodNextIndex,
       "dlmodTable": dlmodTable,
       "dlmodEntry": dlmodEntry,
       "dlmodIndex": dlmodIndex,
       "dlmodName": dlmodName,
       "dlmodPath": dlmodPath,
       "dlmodError": dlmodError,
       "dlmodStatus": dlmodStatus}
)
