# SNMP MIB module (SCTE-HMS-ROOTS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-ROOTS.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:36:31 2025
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

(scteHmsTree,) = mibBuilder.importSymbols(
    "SCTE-ROOT",
    "scteHmsTree")

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

hmsScteRootMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 0)
)
if mibBuilder.loadTexts:
    hmsScteRootMIB.setRevisions(
        ("2008-03-04 00:00",
         "2008-02-04 00:00",
         "2007-08-15 00:00",
         "2007-05-26 17:30")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PropertyIdent_ObjectIdentity = ObjectIdentity
propertyIdent = _PropertyIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1)
)
_AlarmsIdent_ObjectIdentity = ObjectIdentity
alarmsIdent = _AlarmsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 2)
)
_CommonIdent_ObjectIdentity = ObjectIdentity
commonIdent = _CommonIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3)
)
_PsIdent_ObjectIdentity = ObjectIdentity
psIdent = _PsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4)
)
_FnIdent_ObjectIdentity = ObjectIdentity
fnIdent = _FnIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5)
)
_GenIdent_ObjectIdentity = ObjectIdentity
genIdent = _GenIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6)
)
_TransponderInterfaceBusIdent_ObjectIdentity = ObjectIdentity
transponderInterfaceBusIdent = _TransponderInterfaceBusIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 7)
)
_DownloadIdent_ObjectIdentity = ObjectIdentity
downloadIdent = _DownloadIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8)
)
_OaIdent_ObjectIdentity = ObjectIdentity
oaIdent = _OaIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 9)
)
_RfAmplifierIdent_ObjectIdentity = ObjectIdentity
rfAmplifierIdent = _RfAmplifierIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 10)
)
_InsidePlantIdent_ObjectIdentity = ObjectIdentity
insidePlantIdent = _InsidePlantIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11)
)
_VoipIdent_ObjectIdentity = ObjectIdentity
voipIdent = _VoipIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 12)
)
_MultiMediaIdent_ObjectIdentity = ObjectIdentity
multiMediaIdent = _MultiMediaIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 13)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-ROOTS",
    **{"hmsScteRootMIB": hmsScteRootMIB,
       "propertyIdent": propertyIdent,
       "alarmsIdent": alarmsIdent,
       "commonIdent": commonIdent,
       "psIdent": psIdent,
       "fnIdent": fnIdent,
       "genIdent": genIdent,
       "transponderInterfaceBusIdent": transponderInterfaceBusIdent,
       "downloadIdent": downloadIdent,
       "oaIdent": oaIdent,
       "rfAmplifierIdent": rfAmplifierIdent,
       "insidePlantIdent": insidePlantIdent,
       "voipIdent": voipIdent,
       "multiMediaIdent": multiMediaIdent}
)
