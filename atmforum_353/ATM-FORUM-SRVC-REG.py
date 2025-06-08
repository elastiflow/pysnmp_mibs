# SNMP MIB module (ATM-FORUM-SRVC-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/atmforum_353/ATM-FORUM-TC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:03:59 2025
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

(AtmAddress,
 atmfSrvcRegTypes,
 atmfSrvcRegistryGroup) = mibBuilder.importSymbols(
    "ATM-FORUM-TC-MIB",
    "AtmAddress",
    "atmfSrvcRegTypes",
    "atmfSrvcRegistryGroup")

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

_AtmfSrvcRegLecs_ObjectIdentity = ObjectIdentity
atmfSrvcRegLecs = _AtmfSrvcRegLecs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 5, 1)
)
_AtmfSrvcRegAns_ObjectIdentity = ObjectIdentity
atmfSrvcRegAns = _AtmfSrvcRegAns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 5, 2)
)
_AtmfSrvcRegTable_Object = MibTable
atmfSrvcRegTable = _AtmfSrvcRegTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 8, 1)
)
if mibBuilder.loadTexts:
    atmfSrvcRegTable.setStatus("mandatory")
_AtmfSrvcRegEntry_Object = MibTableRow
atmfSrvcRegEntry = _AtmfSrvcRegEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 8, 1, 1)
)
atmfSrvcRegEntry.setIndexNames(
    (0, "ATM-FORUM-SRVC-REG", "atmfSrvcRegPort"),
    (0, "ATM-FORUM-SRVC-REG", "atmfSrvcRegServiceID"),
    (0, "ATM-FORUM-SRVC-REG", "atmfSrvcRegAddressIndex"),
)
if mibBuilder.loadTexts:
    atmfSrvcRegEntry.setStatus("mandatory")


class _AtmfSrvcRegPort_Type(Integer32):
    """Custom type atmfSrvcRegPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfSrvcRegPort_Type.__name__ = "Integer32"
_AtmfSrvcRegPort_Object = MibTableColumn
atmfSrvcRegPort = _AtmfSrvcRegPort_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 8, 1, 1, 1),
    _AtmfSrvcRegPort_Type()
)
atmfSrvcRegPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfSrvcRegPort.setStatus("mandatory")
_AtmfSrvcRegServiceID_Type = ObjectIdentifier
_AtmfSrvcRegServiceID_Object = MibTableColumn
atmfSrvcRegServiceID = _AtmfSrvcRegServiceID_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 8, 1, 1, 2),
    _AtmfSrvcRegServiceID_Type()
)
atmfSrvcRegServiceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfSrvcRegServiceID.setStatus("mandatory")
_AtmfSrvcRegATMAddress_Type = AtmAddress
_AtmfSrvcRegATMAddress_Object = MibTableColumn
atmfSrvcRegATMAddress = _AtmfSrvcRegATMAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 8, 1, 1, 3),
    _AtmfSrvcRegATMAddress_Type()
)
atmfSrvcRegATMAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfSrvcRegATMAddress.setStatus("mandatory")


class _AtmfSrvcRegAddressIndex_Type(Integer32):
    """Custom type atmfSrvcRegAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmfSrvcRegAddressIndex_Type.__name__ = "Integer32"
_AtmfSrvcRegAddressIndex_Object = MibTableColumn
atmfSrvcRegAddressIndex = _AtmfSrvcRegAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 8, 1, 1, 4),
    _AtmfSrvcRegAddressIndex_Type()
)
atmfSrvcRegAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfSrvcRegAddressIndex.setStatus("mandatory")


class _AtmfSrvcRegParm1_Type(OctetString):
    """Custom type atmfSrvcRegParm1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AtmfSrvcRegParm1_Type.__name__ = "OctetString"
_AtmfSrvcRegParm1_Object = MibTableColumn
atmfSrvcRegParm1 = _AtmfSrvcRegParm1_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 8, 1, 1, 5),
    _AtmfSrvcRegParm1_Type()
)
atmfSrvcRegParm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfSrvcRegParm1.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATM-FORUM-SRVC-REG",
    **{"atmfSrvcRegLecs": atmfSrvcRegLecs,
       "atmfSrvcRegAns": atmfSrvcRegAns,
       "atmfSrvcRegTable": atmfSrvcRegTable,
       "atmfSrvcRegEntry": atmfSrvcRegEntry,
       "atmfSrvcRegPort": atmfSrvcRegPort,
       "atmfSrvcRegServiceID": atmfSrvcRegServiceID,
       "atmfSrvcRegATMAddress": atmfSrvcRegATMAddress,
       "atmfSrvcRegAddressIndex": atmfSrvcRegAddressIndex,
       "atmfSrvcRegParm1": atmfSrvcRegParm1}
)
