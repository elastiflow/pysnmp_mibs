# SNMP MIB module (ZYXEL-ES-ZyxelAPMgmt) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-ES-ZyxelAPMgmt.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:16:50 2025
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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelAPMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _OperationMode_Type(Integer32):
    """Custom type operationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("standalone", 1),
          ("controller", 2),
          ("managed", 3))
    )


_OperationMode_Type.__name__ = "Integer32"
_OperationMode_Object = MibScalar
operationMode = _OperationMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 4, 1),
    _OperationMode_Type()
)
operationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationMode.setStatus("current")
_WlanAPTx_Type = Counter64
_WlanAPTx_Object = MibScalar
wlanAPTx = _WlanAPTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 4, 2),
    _WlanAPTx_Type()
)
wlanAPTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPTx.setStatus("current")
_WlanAPRx_Type = Counter64
_WlanAPRx_Object = MibScalar
wlanAPRx = _WlanAPRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 4, 3),
    _WlanAPRx_Type()
)
wlanAPRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPRx.setStatus("current")
_WlanAPDescription_Type = DisplayString
_WlanAPDescription_Object = MibScalar
wlanAPDescription = _WlanAPDescription_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 4, 4),
    _WlanAPDescription_Type()
)
wlanAPDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPDescription.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-ES-ZyxelAPMgmt",
    **{"zyxelAPMgmt": zyxelAPMgmt,
       "operationMode": operationMode,
       "wlanAPTx": wlanAPTx,
       "wlanAPRx": wlanAPRx,
       "wlanAPDescription": wlanAPDescription}
)
