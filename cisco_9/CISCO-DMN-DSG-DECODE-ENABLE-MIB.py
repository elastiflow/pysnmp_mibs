# SNMP MIB module (CISCO-DMN-DSG-DECODE-ENABLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-DMN-DSG-DECODE-ENABLE-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:04:32 2025
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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

ciscoDSGDecodeEnable = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 13)
)
if mibBuilder.loadTexts:
    ciscoDSGDecodeEnable.setRevisions(
        ("2010-08-30 06:00",
         "2009-12-07 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DecodeEnableTable_Object = MibTable
decodeEnableTable = _DecodeEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 13, 1)
)
if mibBuilder.loadTexts:
    decodeEnableTable.setStatus("current")
_DecodeEnableEntry_Object = MibTableRow
decodeEnableEntry = _DecodeEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 13, 1, 1)
)
decodeEnableEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-DECODE-ENABLE-MIB", "decodeType"),
)
if mibBuilder.loadTexts:
    decodeEnableEntry.setStatus("current")


class _DecodeType_Type(Integer32):
    """Custom type decodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("video", 1),
          ("audio1", 2),
          ("audio2", 3),
          ("audio3", 4),
          ("audio4", 5),
          ("vbi", 6),
          ("data", 7),
          ("mpe1", 8),
          ("mpe2", 9),
          ("mpe3", 10),
          ("mpe4", 11),
          ("mpe5", 12),
          ("stt", 13),
          ("dpi", 14))
    )


_DecodeType_Type.__name__ = "Integer32"
_DecodeType_Object = MibTableColumn
decodeType = _DecodeType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 13, 1, 1, 1),
    _DecodeType_Type()
)
decodeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    decodeType.setStatus("current")


class _DecodeEnable_Type(Integer32):
    """Custom type decodeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DecodeEnable_Type.__name__ = "Integer32"
_DecodeEnable_Object = MibTableColumn
decodeEnable = _DecodeEnable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 13, 1, 1, 2),
    _DecodeEnable_Type()
)
decodeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decodeEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-DECODE-ENABLE-MIB",
    **{"ciscoDSGDecodeEnable": ciscoDSGDecodeEnable,
       "decodeEnableTable": decodeEnableTable,
       "decodeEnableEntry": decodeEnableEntry,
       "decodeType": decodeType,
       "decodeEnable": decodeEnable}
)
