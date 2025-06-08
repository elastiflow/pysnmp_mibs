# SNMP MIB module (METEL-INTERNAL-USM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/metel_38616/METEL-INTERNAL-USM-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:24:38 2025
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

(device,) = mibBuilder.importSymbols(
    "METEL-MIB",
    "device")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

internal_usm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 38616, 1, 779)
)
if mibBuilder.loadTexts:
    internal_usm.setRevisions(
        ("2022-08-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsmUsersAuthPriv_ObjectIdentity = ObjectIdentity
usmUsersAuthPriv = _UsmUsersAuthPriv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38616, 1, 779, 1)
)
_UserTable_Object = MibTable
userTable = _UserTable_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 779, 1, 1)
)
if mibBuilder.loadTexts:
    userTable.setStatus("current")
_UserEntry_Object = MibTableRow
userEntry = _UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 779, 1, 1, 1)
)
userEntry.setIndexNames(
    (0, "METEL-INTERNAL-USM-MIB", "rowIndex"),
)
if mibBuilder.loadTexts:
    userEntry.setStatus("current")
_RowIndex_Type = Integer32
_RowIndex_Object = MibTableColumn
rowIndex = _RowIndex_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 779, 1, 1, 1, 1),
    _RowIndex_Type()
)
rowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rowIndex.setStatus("current")
_UserName_Type = OctetString
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 779, 1, 1, 1, 2),
    _UserName_Type()
)
userName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userName.setStatus("current")


class _UsmUserAuthProtocol_Type(Integer32):
    """Custom type usmUserAuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("md5", 1),
          ("sha1", 2),
          ("sha224", 3),
          ("sha256", 4),
          ("sha384", 5),
          ("sha512", 6))
    )


_UsmUserAuthProtocol_Type.__name__ = "Integer32"
_UsmUserAuthProtocol_Object = MibTableColumn
usmUserAuthProtocol = _UsmUserAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 779, 1, 1, 1, 3),
    _UsmUserAuthProtocol_Type()
)
usmUserAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usmUserAuthProtocol.setStatus("current")


class _UsmUserPrivProtocol_Type(Integer32):
    """Custom type usmUserPrivProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("des", 1),
          ("aes128", 2),
          ("aes192", 3),
          ("aes256", 4),
          ("3des", 5))
    )


_UsmUserPrivProtocol_Type.__name__ = "Integer32"
_UsmUserPrivProtocol_Object = MibTableColumn
usmUserPrivProtocol = _UsmUserPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 779, 1, 1, 1, 4),
    _UsmUserPrivProtocol_Type()
)
usmUserPrivProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usmUserPrivProtocol.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "METEL-INTERNAL-USM-MIB",
    **{"internal-usm": internal_usm,
       "usmUsersAuthPriv": usmUsersAuthPriv,
       "userTable": userTable,
       "userEntry": userEntry,
       "rowIndex": rowIndex,
       "userName": userName,
       "usmUserAuthProtocol": usmUserAuthProtocol,
       "usmUserPrivProtocol": usmUserPrivProtocol}
)
