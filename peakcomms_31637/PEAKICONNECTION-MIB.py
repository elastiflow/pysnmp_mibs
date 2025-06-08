# SNMP MIB module (PEAKICONNECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKICONNECTION-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:49:02 2025
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

(converters,) = mibBuilder.importSymbols(
    "PEAKDEFINITIONS-MIB",
    "converters")

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

peakIConnectionModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 12)
)
if mibBuilder.loadTexts:
    peakIConnectionModule.setRevisions(
        ("2015-09-15 09:00",
         "2014-06-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IConnectionTransmit_ObjectIdentity = ObjectIdentity
iConnectionTransmit = _IConnectionTransmit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 12, 1)
)
_TxIF_Type = OctetString
_TxIF_Object = MibScalar
txIF = _TxIF_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 12, 1, 1),
    _TxIF_Type()
)
txIF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txIF.setStatus("current")
_TxModem_Type = OctetString
_TxModem_Object = MibScalar
txModem = _TxModem_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 12, 1, 2),
    _TxModem_Type()
)
txModem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txModem.setStatus("current")
_IConnectionReceive_ObjectIdentity = ObjectIdentity
iConnectionReceive = _IConnectionReceive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 12, 2)
)
_RxIF_Type = OctetString
_RxIF_Object = MibScalar
rxIF = _RxIF_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 12, 2, 1),
    _RxIF_Type()
)
rxIF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rxIF.setStatus("current")
_RxModem_Type = OctetString
_RxModem_Object = MibScalar
rxModem = _RxModem_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 12, 2, 2),
    _RxModem_Type()
)
rxModem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rxModem.setStatus("current")
_IConnectionConvGroups_ObjectIdentity = ObjectIdentity
iConnectionConvGroups = _IConnectionConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 12, 10)
)
_IConnectionConvConformance_ObjectIdentity = ObjectIdentity
iConnectionConvConformance = _IConnectionConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 12, 11)
)

# Managed Objects groups

iConnectionCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 12, 10, 1)
)
iConnectionCNFReqGrp.setObjects(
      *(("PEAKICONNECTION-MIB", "txIF"),
        ("PEAKICONNECTION-MIB", "txModem"),
        ("PEAKICONNECTION-MIB", "rxIF"),
        ("PEAKICONNECTION-MIB", "rxModem"))
)
if mibBuilder.loadTexts:
    iConnectionCNFReqGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

iConnectionCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 12, 11, 1)
)
iConnectionCNFCompliance.setObjects(
    ("PEAKICONNECTION-MIB", "iConnectionCNFReqGrp")
)
if mibBuilder.loadTexts:
    iConnectionCNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKICONNECTION-MIB",
    **{"peakIConnectionModule": peakIConnectionModule,
       "iConnectionTransmit": iConnectionTransmit,
       "txIF": txIF,
       "txModem": txModem,
       "iConnectionReceive": iConnectionReceive,
       "rxIF": rxIF,
       "rxModem": rxModem,
       "iConnectionConvGroups": iConnectionConvGroups,
       "iConnectionCNFReqGrp": iConnectionCNFReqGrp,
       "iConnectionConvConformance": iConnectionConvConformance,
       "iConnectionCNFCompliance": iConnectionCNFCompliance}
)
