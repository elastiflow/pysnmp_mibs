# SNMP MIB module (JUNIPER-LSYSVD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-LSYSVD-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:50:22 2025
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

(jnxLsysVD,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxLsysVD")

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

jnxLSYSVDMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 24, 1)
)
if mibBuilder.loadTexts:
    jnxLSYSVDMIB.setRevisions(
        ("2021-02-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class LsysVDIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_JnxLSYSVDObjects_ObjectIdentity = ObjectIdentity
jnxLSYSVDObjects = _JnxLSYSVDObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 24, 1, 1)
)
_JnxLSYSVDBasicInfoTable_Object = MibTable
jnxLSYSVDBasicInfoTable = _JnxLSYSVDBasicInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 24, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxLSYSVDBasicInfoTable.setStatus("current")
_JnxLSYSVDBasicInfoEntry_Object = MibTableRow
jnxLSYSVDBasicInfoEntry = _JnxLSYSVDBasicInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 24, 1, 1, 1, 1)
)
jnxLSYSVDBasicInfoEntry.setIndexNames(
    (0, "JUNIPER-LSYSVD-MIB", "jnxLSYSVDKey"),
)
if mibBuilder.loadTexts:
    jnxLSYSVDBasicInfoEntry.setStatus("current")
_JnxLSYSVDKey_Type = LsysVDIndex
_JnxLSYSVDKey_Object = MibTableColumn
jnxLSYSVDKey = _JnxLSYSVDKey_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 24, 1, 1, 1, 1, 1),
    _JnxLSYSVDKey_Type()
)
jnxLSYSVDKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLSYSVDKey.setStatus("current")


class _JnxLSYSVDName_Type(DisplayString):
    """Custom type jnxLSYSVDName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLSYSVDName_Type.__name__ = "DisplayString"
_JnxLSYSVDName_Object = MibTableColumn
jnxLSYSVDName = _JnxLSYSVDName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 24, 1, 1, 1, 1, 2),
    _JnxLSYSVDName_Type()
)
jnxLSYSVDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLSYSVDName.setStatus("current")


class _JnxLSYSVDMode_Type(Integer32):
    """Custom type jnxLSYSVDMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("root", 0),
          ("logical-system", 1),
          ("tenant-system", 2))
    )


_JnxLSYSVDMode_Type.__name__ = "Integer32"
_JnxLSYSVDMode_Object = MibTableColumn
jnxLSYSVDMode = _JnxLSYSVDMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 24, 1, 1, 1, 1, 3),
    _JnxLSYSVDMode_Type()
)
jnxLSYSVDMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLSYSVDMode.setStatus("current")


class _JnxLSYSVDSecProfileName_Type(DisplayString):
    """Custom type jnxLSYSVDSecProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxLSYSVDSecProfileName_Type.__name__ = "DisplayString"
_JnxLSYSVDSecProfileName_Object = MibTableColumn
jnxLSYSVDSecProfileName = _JnxLSYSVDSecProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 24, 1, 1, 1, 1, 4),
    _JnxLSYSVDSecProfileName_Type()
)
jnxLSYSVDSecProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLSYSVDSecProfileName.setStatus("current")
_JnxLSYSVDSummary_ObjectIdentity = ObjectIdentity
jnxLSYSVDSummary = _JnxLSYSVDSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 24, 1, 2)
)
_JnxLSYSVDLsysCount_Type = Unsigned32
_JnxLSYSVDLsysCount_Object = MibScalar
jnxLSYSVDLsysCount = _JnxLSYSVDLsysCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 24, 1, 2, 1),
    _JnxLSYSVDLsysCount_Type()
)
jnxLSYSVDLsysCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLSYSVDLsysCount.setStatus("current")
_JnxLSYSVDTsysCount_Type = Unsigned32
_JnxLSYSVDTsysCount_Object = MibScalar
jnxLSYSVDTsysCount = _JnxLSYSVDTsysCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 24, 1, 2, 2),
    _JnxLSYSVDTsysCount_Type()
)
jnxLSYSVDTsysCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLSYSVDTsysCount.setStatus("current")
_JnxLSYSVDSecProfileCount_Type = Unsigned32
_JnxLSYSVDSecProfileCount_Object = MibScalar
jnxLSYSVDSecProfileCount = _JnxLSYSVDSecProfileCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 24, 1, 2, 3),
    _JnxLSYSVDSecProfileCount_Type()
)
jnxLSYSVDSecProfileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLSYSVDSecProfileCount.setStatus("current")
_JnxLSYSVDLsysMaximum_Type = Unsigned32
_JnxLSYSVDLsysMaximum_Object = MibScalar
jnxLSYSVDLsysMaximum = _JnxLSYSVDLsysMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 24, 1, 2, 4),
    _JnxLSYSVDLsysMaximum_Type()
)
jnxLSYSVDLsysMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLSYSVDLsysMaximum.setStatus("current")
_JnxLSYSVDTsysMaximum_Type = Unsigned32
_JnxLSYSVDTsysMaximum_Object = MibScalar
jnxLSYSVDTsysMaximum = _JnxLSYSVDTsysMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 24, 1, 2, 5),
    _JnxLSYSVDTsysMaximum_Type()
)
jnxLSYSVDTsysMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLSYSVDTsysMaximum.setStatus("current")
_JnxLSYSVDSecProfileMaximum_Type = Unsigned32
_JnxLSYSVDSecProfileMaximum_Object = MibScalar
jnxLSYSVDSecProfileMaximum = _JnxLSYSVDSecProfileMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 24, 1, 2, 6),
    _JnxLSYSVDSecProfileMaximum_Type()
)
jnxLSYSVDSecProfileMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLSYSVDSecProfileMaximum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-LSYSVD-MIB",
    **{"LsysVDIndex": LsysVDIndex,
       "jnxLSYSVDMIB": jnxLSYSVDMIB,
       "jnxLSYSVDObjects": jnxLSYSVDObjects,
       "jnxLSYSVDBasicInfoTable": jnxLSYSVDBasicInfoTable,
       "jnxLSYSVDBasicInfoEntry": jnxLSYSVDBasicInfoEntry,
       "jnxLSYSVDKey": jnxLSYSVDKey,
       "jnxLSYSVDName": jnxLSYSVDName,
       "jnxLSYSVDMode": jnxLSYSVDMode,
       "jnxLSYSVDSecProfileName": jnxLSYSVDSecProfileName,
       "jnxLSYSVDSummary": jnxLSYSVDSummary,
       "jnxLSYSVDLsysCount": jnxLSYSVDLsysCount,
       "jnxLSYSVDTsysCount": jnxLSYSVDTsysCount,
       "jnxLSYSVDSecProfileCount": jnxLSYSVDSecProfileCount,
       "jnxLSYSVDLsysMaximum": jnxLSYSVDLsysMaximum,
       "jnxLSYSVDTsysMaximum": jnxLSYSVDTsysMaximum,
       "jnxLSYSVDSecProfileMaximum": jnxLSYSVDSecProfileMaximum}
)
