# SNMP MIB module (DIGI-SECUREACCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-SECUREACCESS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:54:31 2025
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

(digiSecureAccess,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiSecureAccess")

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



class Switch(Integer32):
    """Custom type Switch based on Integer32"""
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
          ("notSupported", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SecureAccessSSH_Type = Switch
_SecureAccessSSH_Object = MibScalar
secureAccessSSH = _SecureAccessSSH_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 15, 1),
    _SecureAccessSSH_Type()
)
secureAccessSSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secureAccessSSH.setStatus("mandatory")
_SecureAccessTelnet_Type = Switch
_SecureAccessTelnet_Object = MibScalar
secureAccessTelnet = _SecureAccessTelnet_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 15, 2),
    _SecureAccessTelnet_Type()
)
secureAccessTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secureAccessTelnet.setStatus("mandatory")
_SecureAccessHTTP_Type = Switch
_SecureAccessHTTP_Object = MibScalar
secureAccessHTTP = _SecureAccessHTTP_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 15, 3),
    _SecureAccessHTTP_Type()
)
secureAccessHTTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secureAccessHTTP.setStatus("mandatory")
_SecureAccessRLogin_Type = Switch
_SecureAccessRLogin_Object = MibScalar
secureAccessRLogin = _SecureAccessRLogin_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 15, 4),
    _SecureAccessRLogin_Type()
)
secureAccessRLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secureAccessRLogin.setStatus("mandatory")
_SecureAccessRSH_Type = Switch
_SecureAccessRSH_Object = MibScalar
secureAccessRSH = _SecureAccessRSH_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 15, 5),
    _SecureAccessRSH_Type()
)
secureAccessRSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secureAccessRSH.setStatus("mandatory")
_SecureAccessRealport_Type = Switch
_SecureAccessRealport_Object = MibScalar
secureAccessRealport = _SecureAccessRealport_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 15, 6),
    _SecureAccessRealport_Type()
)
secureAccessRealport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secureAccessRealport.setStatus("mandatory")
_SecureAccessReverseTCP_Type = Switch
_SecureAccessReverseTCP_Object = MibScalar
secureAccessReverseTCP = _SecureAccessReverseTCP_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 15, 7),
    _SecureAccessReverseTCP_Type()
)
secureAccessReverseTCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secureAccessReverseTCP.setStatus("mandatory")
_SecureAccessReverseTelnet_Type = Switch
_SecureAccessReverseTelnet_Object = MibScalar
secureAccessReverseTelnet = _SecureAccessReverseTelnet_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 15, 8),
    _SecureAccessReverseTelnet_Type()
)
secureAccessReverseTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secureAccessReverseTelnet.setStatus("mandatory")
_SecureAccessSecureRealPort_Type = Switch
_SecureAccessSecureRealPort_Object = MibScalar
secureAccessSecureRealPort = _SecureAccessSecureRealPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 15, 9),
    _SecureAccessSecureRealPort_Type()
)
secureAccessSecureRealPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secureAccessSecureRealPort.setStatus("mandatory")
_SecureAccessHTTPS_Type = Switch
_SecureAccessHTTPS_Object = MibScalar
secureAccessHTTPS = _SecureAccessHTTPS_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 15, 10),
    _SecureAccessHTTPS_Type()
)
secureAccessHTTPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secureAccessHTTPS.setStatus("mandatory")
_SecureAccessSSL_Type = Switch
_SecureAccessSSL_Object = MibScalar
secureAccessSSL = _SecureAccessSSL_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 15, 11),
    _SecureAccessSSL_Type()
)
secureAccessSSL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secureAccessSSL.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-SECUREACCESS-MIB",
    **{"Switch": Switch,
       "secureAccessSSH": secureAccessSSH,
       "secureAccessTelnet": secureAccessTelnet,
       "secureAccessHTTP": secureAccessHTTP,
       "secureAccessRLogin": secureAccessRLogin,
       "secureAccessRSH": secureAccessRSH,
       "secureAccessRealport": secureAccessRealport,
       "secureAccessReverseTCP": secureAccessReverseTCP,
       "secureAccessReverseTelnet": secureAccessReverseTelnet,
       "secureAccessSecureRealPort": secureAccessSecureRealPort,
       "secureAccessHTTPS": secureAccessHTTPS,
       "secureAccessSSL": secureAccessSSL}
)
